import matplotlib.pyplot as plt
import math


def gradient(p):

	x_plus_iso = trilinear(1, 0.5, 0.5, p)
	x_minus_iso = trilinear(0, 0.5, 0.5, p)

	grad_x = x_plus_iso - x_minus_iso

	y_plus_iso = trilinear(0.5, 0.5, 1, p)
	y_minus_iso = trilinear(0.5, 0.5, 0, p)

	grad_y = y_plus_iso - y_minus_iso

	z_plus_iso = trilinear(0.5, 1, 0.5, p)
	z_minus_iso = trilinear(0.5, 0, 0.5, p)

	grad_z = z_plus_iso - z_minus_iso

	grad_magnitude = math.sqrt(grad_x**2 + grad_y**2 + grad_z**2)

	return grad_magnitude


def trilinear(r, s, t, p):
	w0 = (1-r)*(1-s)*(1-t)
	w1 = r*(1-s)*(1-t)
	w2 = (1-r)*s*(1-t)
	w3 = r*s*(1-t)
	w4 = (1-r)*(1-s)*t
	w5 = r*(1-s)*t
	w6 = (1-r)*s*t
	w7 = r*s*t

	iso = w0*p[0] + w1*p[1] + w2*p[2] + w3*p[3] + w4*p[4] + w5*p[5] + w6*p[6] + w7*p[7]
	return iso


"""f = open("tooth_data.txt", "r")

l = f.readlines()

f.close()


uni_iso = {}
for i in range(0, len(l)):
	t = l[i].split(",")
	#import pdb;pdb.set_trace()
	x = int(t[0].split("\n")[0])
	y = int(t[1].split("\n")[0])
	z = int(t[2].split("\n")[0])
	iso = int(t[3].split("\n")[0])
	if iso not in uni_iso.keys():
		uni_iso[iso] = [[],[],[]]

	uni_iso[iso][0].append(x)
	uni_iso[iso][1].append(y)
	uni_iso[iso][2].append(z)



print(uni_iso[76][0])
for i in uni_iso.keys():
	print(i, len(uni_iso[i]))
	if len(uni_iso[i][0]) > 5000:
		fig = plt.figure()
		ax = plt.axes(projection ="3d")
	 	# Creating plot
		ax.scatter3D(uni_iso[i][0], uni_iso[i][1], uni_iso[i][2], s=0.1, color = "green")
		plt.title("simple 3D scatter plot")
		#plt.savefig("plots/" + str(i) + "_" + str(len(uni_iso[i][0])) + ".png")
		plt.show()
		break"""
