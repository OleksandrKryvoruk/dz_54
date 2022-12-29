# Завдання 1

class Matrix:

    def __init__(self, lst):
        try:
            for i in range(len(lst)):
                if type(lst) == list and type(lst[i]) == list:       
                    if lst == [[]]:
                        self.matrix = [[]]
                        return None
                    for x in lst[i]:
                        if not (type(x) == int or type(x) == float): 
                            print("all elements of matrix must be numbers")
                            self.matrix = [[]]
                            return None
                    self.matrix = lst                            
                else:                                                
                    print("lst isn't list of lists")
                    self.matrix = [[]]
                    return None
        except TypeError:                                   
            print("lst isn't list of lists")
            self.matrix = [[]]

    def __str__(self):
        return self.matrix


    def __matching(self, lst_2):
                                                                      
        lines = len(self.matrix) - len(lst_2.matrix)                  
        if lines > 0:
            for i in range(lines):
                lst_2.matrix.append([])
        elif lines < 0:
            for i in range(lines * (-1)):
                self.matrix.append([])

        for i in range(len(self.matrix)):              
            columns = len(self.matrix[i]) - len(lst_2.matrix[i])
            if columns > 0:
                for j in range(columns):
                    lst_2.matrix[i].append(0)
            elif columns < 0:
                for j in range(columns * (-1)):
                    self.matrix[i].append(0)              

        num_members = 0
        for i in range(len(self.matrix)):
            if num_members < len(self.matrix[i]) or num_members < len(lst_2.matrix[i]):
                if len(self.matrix[i]) >= len(lst_2.matrix[i]):
                    num_members = len(self.matrix[i])
                elif len(self.matrix[i]) < len(lst_2.matrix[i]):
                    num_members = len(lst_2.matrix[i])
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) < num_members:
                self.matrix[i].append(0)
            if len(lst_2.matrix[i]) < num_members:
                lst_2.matrix[i].append(0)


    def __add_digit(self, lst_2):
        if self.matrix == [[]]:
            return None
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + lst_2)
        self.matrix = result

    def __sub_digit(self, lst_2):
        if self.matrix == [[]]:
            return None
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] - lst_2)
        self.matrix = result


    def __mul_digit(self, lst_2):
        if self.matrix == [[]]:
            return None
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] * lst_2)
        self.matrix = result


    def __add_matrix(self, lst_2):
        self.__matching(obj_2)
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + lst_2.matrix[i][j])
        self.matrix = result


    def __sub_matrix(self, lst_2):
        self.__matching(lst_2)
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] - lst_2.matrix[i][j])
        self.matrix = result

    def __mul_matrix(self, lst_2):
        if len(self.matrix[0]) != len(lst_2.matrix):
            print("Imposible to multiply these matrixes!")
            return None
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for i_2 in range(len(lst_2.matrix[0])):
                sum = 0
                for j in range(len(self.matrix[i])):
                    sum += self.matrix[i][j] * lst_2.matrix[j][i_2]
                result[i].append(sum)
        self.matrix = result


    def operations(self, lst_2, oper):
        if type(lst_2) == Matrix:
            if oper == "+":
                self.__add_matrix(lst_2)
            elif oper == "-":
                self.__sub_matrix(lst_2)
            elif oper == "*":
                self.__mul_matrix(lst_2)
            else:
                print("unknown operation")
                return None
        elif type(lst_2) == int or type(lst_2) == float:
            if oper == "+":
                self.__add_digit(lst_2)
            elif oper == "-":
                self.__sub_digit(lst_2)
            elif oper == "*":
                self.__mul_digit(lst_2)
            else:
                print("unknown operation")
                return None
        else:
            print("object from operation with matrix must be digit or matrix")
            return None


    def tranponation(self):
        columns = 0
        lines = 0
        if len(self.matrix) > len(self.matrix[0]):
            columns = len(self.matrix) - len(self.matrix[0])
            for i in range(len(self.matrix)):
                for j in range(columns):
                    self.matrix[i].append(0)
        elif  len(self.matrix) < len(self.matrix[0]):
            lines = len(self.matrix[0]) - len(self.matrix)
            for i in range(lines):
                self.matrix.append([0 for j in range(len(self.matrix[0]))])

        count = 0
        for i in range(len(self.matrix)):
            for j in range(count, len(self.matrix[i])):
                if i != j:

                        self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
            count += 1
        if columns > 0:
            for i in range(columns):
                self.matrix.pop()
        elif lines > 0:
            for i in range(len(self.matrix)):
                for j in range(lines):
                    self.matrix[i].pop()


list_1 = [[1, 2, 3, 4, 6, 7], [8, 9, 0, 1, 2, 3]]
list_2 = [[1, 2], [3, 4], [5, 6]]
list_3 = [[1, 2, 3], [4, 5, 6]]
matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)
matrix_3 = Matrix(list_3)
print("Matrix 1: ", matrix_1.__str__())
print("Matrix 2: ", matrix_2.__str__())
print("Matrix 3: ", matrix_3.__str__())
matrix_2.operations(matrix_3, "*")
print("Matrix_2 after multiply on matrix_3: ", matrix_2.__str__())
matrix_1.tranponation()
print("Matrix_1 after transopation: ", matrix_1.__str__())
