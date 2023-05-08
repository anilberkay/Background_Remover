from rembg import remove

input_file = input("Enter your image path: ")
output_file = "output.png"

with open(input_file,'rb') as i:
    with open(output_file,'wb') as o:
        inp_img = i.read()
        oup_img = remove(inp_img)
        o.write(oup_img)

