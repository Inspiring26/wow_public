import xlrd
import re
import xlwt

def xls2listType2(xlsname,n):#返回单个列表
	data = xlrd.open_workbook(xlsname)
	table = data.sheet_by_index(0)
	nrows = table.nrows
	# print(nrows)
	list0 = []
	# print(list1)
	for x in range(1,nrows):# 从第二行开始
		text_data = table.cell(x,n).value
		
		list0.append(text_data)
	return list0

def write_excel(filename, data):
	pattern = xlwt.Pattern()
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour = 3
	style = xlwt.XFStyle()
	style.pattern = pattern

	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1')
	sheet.write(1,3,data,style)
	book.save(filename)
def write_excel_all(filename,five_B,five_C,five_E,five_F,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q):
	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1')
	c = 0
	for x in range(len(five_B)):
		if int(five_B[x]) in fivexc_E:
			pos = fivexc_E.index(int(five_B[x]))
			if int(five_F[x]) == int(fivexc_Q[pos]):
				sheet.write(c,0,int(five_B[x]))
				sheet.write(c,1,five_C[x])
				sheet.write(c,2,five_E[x])
				sheet.write(c,3,five_F[x])
				c = c +1
				sheet.write(c,0,int(fivexc_D[pos]))
				sheet.write(c,1,fivexc_E[pos])
				sheet.write(c,2,fivexc_H[pos])
				sheet.write(c,3,fivexc_I[pos])
				sheet.write(c,4,fivexc_J[pos])
				sheet.write(c,5,int(fivexc_P[pos]))
				sheet.write(c,6,int(fivexc_Q[pos]))
				c = c +2
	
	book.save(filename)
def write_excel_error(filename,five_B,five_C,five_E,five_F,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q):
	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1')
	c = 0
	for x in range(len(five_B)):
		if int(five_B[x]) in fivexc_E:
			pos = fivexc_E.index(int(five_B[x]))
			if int(five_F[x]) != int(fivexc_Q[pos]):
				
				sheet.write(c,0,int(five_B[x]))
				sheet.write(c,1,five_C[x])
				sheet.write(c,2,five_E[x])
				sheet.write(c,3,five_F[x])
				c = c +1
				sheet.write(c,0,int(fivexc_D[pos]))
				sheet.write(c,1,fivexc_E[pos])
				sheet.write(c,2,fivexc_H[pos])
				sheet.write(c,3,fivexc_I[pos])
				sheet.write(c,4,fivexc_J[pos])
				sheet.write(c,5,int(fivexc_P[pos]))
				sheet.write(c,6,int(fivexc_Q[pos]))
				c = c +2
	
	book.save(filename)

def write_excel_notin(filename,five_B,five_C,five_E,five_F,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q):
	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1')
	c = 0
	for x in range(len(five_B)):
		if int(five_B[x]) not in fivexc_E:	
			sheet.write(c,0,int(five_B[x]))
			sheet.write(c,1,five_C[x])
			sheet.write(c,2,five_E[x])
			sheet.write(c,3,five_F[x])
			c = c +2
				
	
	book.save(filename)
def write_excel_5_color(filename,five_A,five_B,five_C,five_D,five_E,five_F,five_G,five_H,five_I,five_J,five_K,five_L,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q):
	# pattern = xlwt.Pattern()
	# pattern.pattern = xlwt.Pattern.SOLID_PATTERN
	# pattern.pattern_fore_colour = 22
	# style = xlwt.XFStyle()
	# style.pattern = pattern
	# style = xlwt.easyxf('pattern: pattern solid, fore_colour light_green;border: left thin,right thin,top thin,bottom thin')
	style = xlwt.easyxf('pattern: pattern solid, fore_colour light_green')

	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1')
	c = 0
	for x in range(len(five_B)):
		if int(five_B[x]) in fivexc_E:
			pos = fivexc_E.index(int(five_B[x]))
			if int(five_F[x]) == int(fivexc_Q[pos]):
				sheet.write(c,0,int(five_A[x]),style)
				sheet.write(c,1,five_B[x],style)
				sheet.write(c,2,five_C[x],style)
				sheet.write(c,3,five_D[x],style)
				sheet.write(c,4,five_E[x],style)
				sheet.write(c,5,five_F[x],style)
				sheet.write(c,6,five_G[x],style)
				sheet.write(c,7,five_H[x],style)
				sheet.write(c,8,five_I[x],style)
				sheet.write(c,9,five_J[x],style)
				sheet.write(c,10,five_K[x],style)
				sheet.write(c,11,five_L[x],style)
			else:
				sheet.write(c,0,int(five_A[x]))
				sheet.write(c,1,five_B[x])
				sheet.write(c,2,five_C[x])
				sheet.write(c,3,five_D[x])
				sheet.write(c,4,five_E[x])
				sheet.write(c,5,five_F[x])
				sheet.write(c,6,five_G[x])
				sheet.write(c,7,five_H[x])
				sheet.write(c,8,five_I[x])
				sheet.write(c,9,five_J[x])
				sheet.write(c,10,five_K[x])
				sheet.write(c,11,five_L[x])
			c = c +1
		else:
			sheet.write(c,0,int(five_A[x]))
			sheet.write(c,1,five_B[x])
			sheet.write(c,2,five_C[x])
			sheet.write(c,3,five_D[x])
			sheet.write(c,4,five_E[x])
			sheet.write(c,5,five_F[x])
			sheet.write(c,6,five_G[x])
			sheet.write(c,7,five_H[x])
			sheet.write(c,8,five_I[x])
			sheet.write(c,9,five_J[x])
			sheet.write(c,10,five_K[x])
			sheet.write(c,11,five_L[x])
			c = c +1
					
				
	
	book.save(filename)
def write_excel_5xc_color(filename,five_B,five_C,five_E,five_F,fivexc_A, fivexc_D, fivexc_E, fivexc_F, fivexc_G, fivexc_H, fivexc_I, fivexc_J, fivexc_K, fivexc_L, fivexc_M, fivexc_N, fivexc_O, fivexc_P, fivexc_Q, fivexc_R, fivexc_S, fivexc_T, fivexc_U, fivexc_V ):
	# pattern = xlwt.Pattern()
	# pattern.pattern = xlwt.Pattern.SOLID_PATTERN
	# pattern.pattern_fore_colour = 22
	# style = xlwt.XFStyle()
	# style.pattern = pattern
	style = xlwt.easyxf('pattern: pattern solid, fore_colour light_green')

	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1')
	c = 0
	five_B_ = []
	for x in range(len(five_B)):
		five_B_.append(int(five_B[x]))

	for x in range(len(fivexc_E)):

		if fivexc_E[x] in five_B_:
			pos = five_B_.index(int(fivexc_E[x]))
			if int(five_F[pos]) == int(fivexc_Q[x]):
				sheet.write(c,0,fivexc_A[x],style)
				sheet.write(c,1,int(fivexc_D[x]),style)
				sheet.write(c,2,fivexc_E[x],style)
				sheet.write(c,3,fivexc_F[x],style)
				sheet.write(c,4,fivexc_G[x],style)
				sheet.write(c,5,fivexc_H[x],style)
				sheet.write(c,6,fivexc_I[x],style)
				sheet.write(c,7,fivexc_J[x],style)
				sheet.write(c,8,int(fivexc_K[x]),style)
				sheet.write(c,9,fivexc_L[x],style)
				sheet.write(c,10,fivexc_M[x],style)
				sheet.write(c,11,fivexc_N[x],style)
				sheet.write(c,12,fivexc_O[x],style)
				sheet.write(c,13,fivexc_P[x],style)
				sheet.write(c,14,int(fivexc_Q[x]),style)
				sheet.write(c,15,fivexc_R[x],style)
				sheet.write(c,16,int(fivexc_S[x]),style)
				sheet.write(c,17,fivexc_T[x],style)
				sheet.write(c,18,fivexc_U[x],style)
				sheet.write(c,19,fivexc_V[x],style)

			else:
				sheet.write(c,0,fivexc_A[x])
				sheet.write(c,1,int(fivexc_D[x]))
				sheet.write(c,2,fivexc_E[x])
				sheet.write(c,3,fivexc_F[x])
				sheet.write(c,4,fivexc_G[x])
				sheet.write(c,5,fivexc_H[x])
				sheet.write(c,6,fivexc_I[x])
				sheet.write(c,7,fivexc_J[x])
				sheet.write(c,8,int(fivexc_K[x]))
				sheet.write(c,9,fivexc_L[x])
				sheet.write(c,10,fivexc_M[x])
				sheet.write(c,11,fivexc_N[x])
				sheet.write(c,12,fivexc_O[x])
				sheet.write(c,13,fivexc_P[x])
				sheet.write(c,14,int(fivexc_Q[x]))
				sheet.write(c,15,fivexc_R[x])
				sheet.write(c,16,int(fivexc_S[x]))
				sheet.write(c,17,fivexc_T[x])
				sheet.write(c,18,fivexc_U[x])
				sheet.write(c,19,fivexc_V[x])
			c = c +1
		else:
			sheet.write(c,0,fivexc_A[x])
			sheet.write(c,1,int(fivexc_D[x]))
			sheet.write(c,2,fivexc_E[x])
			sheet.write(c,3,fivexc_F[x])
			sheet.write(c,4,fivexc_G[x])
			sheet.write(c,5,fivexc_H[x])
			sheet.write(c,6,fivexc_I[x])
			sheet.write(c,7,fivexc_J[x])
			sheet.write(c,8,int(fivexc_K[x]))
			sheet.write(c,9,fivexc_L[x])
			sheet.write(c,10,fivexc_M[x])
			sheet.write(c,11,fivexc_N[x])
			sheet.write(c,12,fivexc_O[x])
			sheet.write(c,13,fivexc_P[x])
			sheet.write(c,14,int(fivexc_Q[x]))
			sheet.write(c,15,fivexc_R[x])
			sheet.write(c,16,int(fivexc_S[x]))
			sheet.write(c,17,fivexc_T[x])
			sheet.write(c,18,fivexc_U[x])
			sheet.write(c,19,fivexc_V[x])
			c = c +1
					
				
	
	book.save(filename)

def write_excel_notin_but(filename,five_B,five_C,five_E,five_F,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q):
	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1')
	style = xlwt.easyxf('pattern: pattern solid, fore_colour light_green')

	c = 0
	five_B_ = []
	five_C_ = []
	# 符合的名单
	five_C_yes = []
	five_E_ = []
	five_F_ = []
	for x in range(len(five_B)):
		if int(five_B[x]) not in fivexc_E:
			five_B_.append(five_B[x])
			five_C_.append(five_C[x])
			five_E_.append(five_E[x])
			five_F_.append(five_F[x])

			# sheet.write(c,0,int(five_B[x]))
			# sheet.write(c,1,five_C[x])
			# sheet.write(c,2,five_E[x])
			# sheet.write(c,3,five_F[x])
			# c = c +2
	for x in range(len(five_C_)):
		five_C_[x] = five_C_[x].replace("C/O--0C/L转帐","").replace("0C/L转帐 ","").replace(" ","")
		for y in range(len(fivexc_J)):
			if re.search(five_C_[x],fivexc_J[y]) and five_F_[x] == fivexc_Q[y]:
				five_C_yes.append(five_C_[x])
	
	for x in range(len(five_B)):
		if int(five_B[x]) not in fivexc_E:
			urname = five_C[x].replace("C/O--0C/L转帐","").replace("0C/L转帐 ","").replace(" ","")
			if urname in five_C_yes:				
				sheet.write(c,0,int(five_B[x]),style)
				sheet.write(c,1,five_C[x],style)
				sheet.write(c,2,five_E[x],style)
				sheet.write(c,3,five_F[x],style)
				c = c +2
			else:
				sheet.write(c,0,int(five_B[x]))
				sheet.write(c,1,five_C[x])
				sheet.write(c,2,five_E[x])
				sheet.write(c,3,five_F[x])
				c = c +2
	book.save(filename)

if __name__ == '__main__':
	five_A = xls2listType2("5.xls",0)
	five_B = xls2listType2("5.xls",1)
	five_C = xls2listType2("5.xls",2)
	five_D = xls2listType2("5.xls",3)
	five_E = xls2listType2("5.xls",4)
	five_F = xls2listType2("5.xls",5)
	five_G = xls2listType2("5.xls",6)
	five_H = xls2listType2("5.xls",7)
	five_I = xls2listType2("5.xls",8)
	five_J = xls2listType2("5.xls",9)
	five_K = xls2listType2("5.xls",10)
	five_L = xls2listType2("5.xls",11)

	fivexc_A = xls2listType2("5xc.xls",0)
	# fivexc_B
	# fivexc_C
	fivexc_D = xls2listType2("5xc.xls",3)
	fivexc_E = xls2listType2("5xc.xls",4)
	fivexc_F = xls2listType2("5xc.xls",5)
	fivexc_G = xls2listType2("5xc.xls",6)
	fivexc_H = xls2listType2("5xc.xls",7)
	fivexc_I = xls2listType2("5xc.xls",8)
	fivexc_J = xls2listType2("5xc.xls",9)
	fivexc_K = xls2listType2("5xc.xls",10)
	fivexc_L = xls2listType2("5xc.xls",11)
	fivexc_M = xls2listType2("5xc.xls",12)
	fivexc_N = xls2listType2("5xc.xls",13)
	fivexc_O = xls2listType2("5xc.xls",14)
	fivexc_P = xls2listType2("5xc.xls",15)
	fivexc_Q = xls2listType2("5xc.xls",16)
	fivexc_R = xls2listType2("5xc.xls",17)
	fivexc_S = xls2listType2("5xc.xls",18)
	fivexc_T = xls2listType2("5xc.xls",19)
	fivexc_U = xls2listType2("5xc.xls",20)
	fivexc_V = xls2listType2("5xc.xls",21)

	recheck_five_B = list(set(five_B))
	print("前台账号")
	print("总个数："+"\t"+str(len(five_B)))
	print("不重复个数:"+"\t"+str(len(recheck_five_B)))
	repeat = []
	repeat_num = []
	for x in range(len(recheck_five_B)):
		num = five_B.count(recheck_five_B[x])
		if num > 1:
			repeat.append(recheck_five_B[x])
			repeat_num.append(num)
	print(repeat,"\t")
	print(repeat_num,"\t")
	print("\n\n")


	recheck_fivexc_E = list(set(fivexc_E))
	print("确认号")
	print("总个数："+"\t"+str(len(fivexc_E)))
	print("不重复个数:"+"\t"+str(len(recheck_fivexc_E)))
	repeat_xc = []
	repeat_num_xc = []
	for x in range(len(recheck_fivexc_E)):
		num = fivexc_E.count(recheck_fivexc_E[x])
		if num > 1:
			repeat_xc.append(recheck_fivexc_E[x])
			repeat_num_xc.append(num)
	# for x in range(len(repeat_xc)):
	# 	# print(type(repeat_xc[x]))
	# 	print(repeat_xc[x],repeat_num_xc[x])
	
	# print(repeat_xc,"\t")
	# print(repeat_num_xc,"\t")

	


	# print(int(five_B[2]))
	# print(fivexc_E[2])

	write_excel_all("exact_match.xls",five_B,five_C,five_E,five_F,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q)
	write_excel_error("wrong_amount.xls",five_B,five_C,five_E,five_F,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q)
	write_excel_notin("not_in_xc.xls",five_B,five_C,five_E,five_F,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q)
	write_excel_5_color("5_color.xls",five_A,five_B,five_C,five_D,five_E,five_F,five_G,five_H,five_I,five_J,five_K,five_L,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q)
	write_excel_5xc_color("5xc_color.xls",five_B,five_C,five_E,five_F,fivexc_A, fivexc_D, fivexc_E, fivexc_F, fivexc_G, fivexc_H, fivexc_I, fivexc_J, fivexc_K, fivexc_L, fivexc_M, fivexc_N, fivexc_O, fivexc_P, fivexc_Q, fivexc_R, fivexc_S, fivexc_T, fivexc_U, fivexc_V )
	write_excel_notin_but("单号不符合，名字金额符合.xls",five_B,five_C,five_E,five_F,fivexc_D,fivexc_E,fivexc_H,fivexc_I,fivexc_J,fivexc_P,fivexc_Q)




