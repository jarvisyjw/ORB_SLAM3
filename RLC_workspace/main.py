import numpy as np
from scipy.spatial.transform import Rotation as R


def writeinfoMat(infoMat):
    infoMat_str = ""
    for i in range(infoMat.shape[0]):
        # for j in range(infoMat.shape[1]):
            infoMat_str += str(infoMat[i]) + " "
    return infoMat_str

def writePose(pose):
    pose_str = ""
    for i in range(pose.shape[0]):
        pose_str += str(pose[i]) + " "
    return pose_str

# def quat2rot(q):
#     # Convert a quaternion to a rotation matrix
#     q = q / np.linalg.norm(q)
#     q0 = q[0]
#     q1 = q[1]
#     q2 = q[2]
#     q3 = q[3]
#     R = np.array([[q0**2 + q1**2 - q2**2 - q3**2, 2*(q1*q2 - q0*q3), 2*(q1*q3 + q0*q2)],
#                   [2*(q1*q2 + q0*q3), q0**2 - q1**2 + q2**2 - q3**2, 2*(q2*q3 - q0*q1)],
#                   [2*(q1*q3 - q0*q2), 2*(q2*q3 + q0*q1), q0**2 - q1**2 - q2**2 + q3**2]])
#     return R

# def rot2quat(R):
#     # Convert a rotation matrix to a quaternion
#     q = np.zeros(4)
#     q[0] = 0.5 * np.sqrt(1 + R[0, 0] + R[1, 1] + R[2, 2])
#     q[1] = (R[2, 1] - R[1, 2]) / (4 * q[0])
#     q[2] = (R[0, 2] - R[2, 0]) / (4 * q[0])
#     q[3] = (R[1, 0] - R[0, 1]) / (4 * q[0])
#     return np.array(q[1], q[2], q[3], q[0])

def pose2T(pose):
    r = R.from_quat(pose[3:], scalar_first=True)
    T = np.zeros((4, 4))
    T[:3, :3] = r.as_matrix()
    T[:3, 3] = pose[:3]
    T[3, 3] = 1
    return T

def T2pose(T):
    pose = np.zeros(7)
    pose[:3] = T[:3, 3]
    r = R.from_matrix(T[:3, :3])
    pose[3:] = r.as_quat()
    return pose

def calcRelPose(pose1, pose2):
    # Calculate the relative pose between two poses
    T1 = pose2T(pose1)
    T2 = pose2T(pose2)
    # Tw = pose2T([0,0,0,0,0,0,1])
    # relPose = np.dot(Tw, np.linalg.inv(T1), T2)
    relPose = np.dot(np.linalg.inv(T1), T2)
    t = relPose[:3, 3]
    r = R.from_matrix(relPose[:3, :3])
    q = r.as_quat()
    return np.concatenate((t, q))

def parseTraj(filename_traj, filename_g2o, type = "TUM", infoMat = np.array([1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1])):
    if type == "TUM":
        # Load the trajectory
        traj = np.loadtxt(filename_traj)
        # print(traj.shape)
        # print(traj[0, :])

        # Open the g2o file
        with open(filename_g2o, 'w') as g2o:
            # Write the vertices
            for i in range(traj.shape[0]):
                g2o.write('VERTEX_SE3:QUAT {} '.format(i))
                g2o.write(writePose(traj[i, 1:]))
                g2o.write('\n')
            # Write the edges
            for i in range(1, traj.shape[0]):
                relPose = calcRelPose(traj[i-1, 1:], traj[i, 1:])
                g2o.write('EDGE_SE3:QUAT {} {} '.format(i-1, i))
                g2o.write(writePose(relPose))
                g2o.write(writeinfoMat(infoMat))
                g2o.write('\n')
        g2o.close()

    else:
        raise NotImplementedError("Traj Type not Implemented for Transformation!")
    
if __name__ == "__main__":
    filename_traj = "/home/jarvis/jw_ws/SLAM_ws/ORB_SLAM3/Examples_old/ROS/ORB_SLAM3/output/traj/unitysim_traj00.txt"
    filename_g2o = "/home/jarvis/jw_ws/SLAM_ws/ORB_SLAM3/Examples_old/ROS/ORB_SLAM3/output/traj/unitysim_traj00.g2o"
    parseTraj(filename_traj, filename_g2o)