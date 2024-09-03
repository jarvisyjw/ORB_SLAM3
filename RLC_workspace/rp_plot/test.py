import re

def extract_chi2_from_file(input_file,output_file):
    chi2_vals = []

    pattern = re.compile(r'iteration= 11.*?chi2=\s*([0-9.]+)')

    with open(input_file,"r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                chi2_val = float(match.group(1))
                chi2_vals.append(chi2_val)
            
    with open(output_file,"w") as f:
        for idx, chi2_val in enumerate(chi2_vals):
            f.write(f"{idx} {chi2_val}\n")


if __name__ == "__main__":
    # data_name = "city10000"
    # data_name = "manhattan"
    # data_name = "MIT"
    data_name = "ais2klinik"
    # data_name = "kitti_00"
    # data_name = "sphere2500"




    input_file = f"./data/output_data/{data_name}_output.txt"
    output_file = f"./data/rp_data/{data_name}_val.txt"
    extract_chi2_from_file(input_file,output_file)