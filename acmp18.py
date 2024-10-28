input_data = open('input.txt', 'r')
data = input_data.read ()
output_data = open ('output.txt', 'w')
n = int(data)
pr = 1
pr_list=[]
for i in range (1,n+1):
    pr=pr*i
    pr_list.append(pr)
output_data.write(str(pr_list))
input_data.close()
output_data.close()