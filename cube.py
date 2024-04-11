import numpy as np
import copy
from draw import draw_cube_3D

'''
    U
L   F   R   B
    D
'''
class cube():
    def __init__(self) -> None:
        self.state = {
            'U': np.array([['⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜'], ['⬜', '⬜', '⬜']]),
            'F': np.array([['🟩', '🟩', '🟩'], ['🟩', '🟩', '🟩'], ['🟩', '🟩', '🟩']]),
            'R': np.array([['🟥', '🟥', '🟥'], ['🟥', '🟥', '🟥'], ['🟥', '🟥', '🟥']]),
            'B': np.array([['🟦', '🟦', '🟦'], ['🟦', '🟦', '🟦'], ['🟦', '🟦', '🟦']]),
            'L': np.array([['🟧', '🟧', '🟧'], ['🟧', '🟧', '🟧'], ['🟧', '🟧', '🟧']]),
            'D': np.array([['🟨', '🟨', '🟨'], ['🟨', '🟨', '🟨'], ['🟨', '🟨', '🟨']])
        }
        self.faces = list(self.state.keys())
        self.loc = {'L':'L', 'R':'R', 'F':'F', 'B':'B', 'U':'U', 'D':'D'}  # up = white 
        # self.loc = {'L':'R', 'R':'L', 'F':'B', 'B':'F', 'U':'D', 'D':'U'}  # up = yellow
    
    def rotate_face(self, face):  # 顺时针旋转当前面
        tmp = copy.deepcopy(self.state[face])
        self.state[face][0][0], self.state[face][0][2], self.state[face][2][2], self.state[face][2][0] = tmp[2][0],  tmp[0][0],  tmp[0][2],  tmp[2][2]
        self.state[face][0][1], self.state[face][1][2], self.state[face][2][1], self.state[face][1][0] = tmp[1][0],  tmp[0][1],  tmp[1][2],  tmp[2][1]

    def rotate_side(self, face):  # 顺时针旋转对应侧面
        tmp = copy.deepcopy(self.state)
        if face == 'U':
            self.state['L'][0], self.state['F'][0], self.state['R'][0], self.state['B'][0] = \
             tmp['F'][0],  tmp['R'][0],  tmp['B'][0, :],  tmp['L'][0, :]
        elif face == 'D':
            self.state['L'][2], self.state['F'][2], self.state['R'][2], self.state['B'][2] = \
             tmp['B'][2, :],  tmp['L'][2],  tmp['F'][2],  tmp['R'][2, :]
        elif face == 'L':
            self.state['U'][:, 0], self.state['F'][:, 0], self.state['D'][:, 0], self.state['B'][:, 2] = \
             tmp['B'][[2, 1, 0], 2],  tmp['U'][:, 0],  tmp['F'][:, 0],  tmp['D'][[2, 1, 0], 0]
        elif face == 'R':
            self.state['U'][:, 2], self.state['F'][:, 2], self.state['D'][:, 2], self.state['B'][:, 0] = \
             tmp['F'][:, 2],  tmp['D'][:, 2],  tmp['B'][[2, 1, 0], 0],  tmp['U'][[2, 1, 0], 2]
        elif face == 'F':
            self.state['U'][2, :], self.state['R'][:, 0], self.state['D'][0, :], self.state['L'][:, 2] = \
             tmp['L'][[2, 1, 0], 2],  tmp['U'][2, :],  tmp['R'][[2, 1, 0], 0],  tmp['D'][0, :]
        elif face == 'B':
            self.state['U'][0, :], self.state['R'][:, 2], self.state['D'][2, :], self.state['L'][:, 0] = \
             tmp['R'][:, 2],  tmp['D'][2, [2, 1, 0]],  tmp['L'][:, 0],  tmp['U'][0, [2, 1, 0]]
    
    def rotate_loc(self, axis):  # 整体旋转cube
        def rotate_180(matrix):
            horizontal_flip = [row[::-1] for row in matrix]
            vertical_flip = horizontal_flip[::-1]
            return np.array(vertical_flip)
        def rotate_90(matrix):
            transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
            rotated_matrix = [row[::-1] for row in transposed_matrix]
            return np.array(rotated_matrix)
        def rotate_270(matrix):
            transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
            rotated_matrix = transposed_matrix[::-1]
            return np.array(rotated_matrix)
        tmp = copy.deepcopy(self.state)
        if axis == 'x':
            self.state['F'], self.state['U'], self.state['B'], self.state['D'] = tmp['D'], tmp['F'], rotate_180(tmp['U']), rotate_180(tmp['B'])
            self.state['L'], self.state['R'] = rotate_270(tmp['L']), rotate_90(tmp['R'])
        elif axis == 'y':
            self.state['F'], self.state['L'], self.state['B'], self.state['R'] = tmp['R'], tmp['F'], tmp['L'], tmp['B']
            self.state['D'], self.state['U'] = rotate_270(tmp['D']), rotate_90(tmp['U'])
        elif axis == 'z':
            self.state['U'], self.state['R'], self.state['D'], self.state['L'] = rotate_90(tmp['L']), rotate_90(tmp['U']), rotate_90(tmp['R']), rotate_90(tmp['B'])
            self.state['B'], self.state['F'] = rotate_270(tmp['B']), rotate_90(tmp['F'])


    def rotate(self, move, times):
        back = {'u':'Dy', 'd':'Uy', 'l':'Rx', 'r':'Lx', 'f':'Bz', 'b':'Fz'}
        for i in range(times):
            if move in 'xyz':
                self.rotate_loc(move)
            elif move in 'UDLRFB':
                self.rotate_face(move)
                self.rotate_side(move)
            elif move in 'udlrfb':
                self.rotate_face(back[move][0]), self.rotate_side(back[move][0])
                if move in 'urf':
                    self.rotate_loc(back[move][1])
                else:
                    self.rotate_loc(back[move][1]), self.rotate_loc(back[move][1]), self.rotate_loc(back[move][1])
            elif move in 'EMS':
                if move == 'E':
                    self.rotate_face('U'), self.rotate_side('U')
                    self.rotate_face('D'), self.rotate_side('D'), self.rotate_face('D'), self.rotate_side('D'), self.rotate_face('D'), self.rotate_side('D')
                    self.rotate_loc('y'), self.rotate_loc('y'), self.rotate_loc('y')
                elif move == 'M':
                    self.rotate_face('R'), self.rotate_side('R')
                    self.rotate_face('L'), self.rotate_side('L'), self.rotate_face('L'), self.rotate_side('L'), self.rotate_face('L'), self.rotate_side('L')
                    self.rotate_loc('x'), self.rotate_loc('x'), self.rotate_loc('x')
                elif move == 'S':
                    self.rotate_face('B'), self.rotate_side('B')
                    self.rotate_face('F'), self.rotate_side('F'), self.rotate_face('F'), self.rotate_side('F'), self.rotate_face('F'), self.rotate_side('F')
                    self.rotate_loc('z')


    def run(self, s):
        s = s.replace(" ", "")
        s += '#'
        i = 0
        while 1:
            if s[i] == '#':
                break
            if s[i] in '()':  # to be fixed
                i += 1
                continue
            face = s[i]
            if s[i + 1] == "'":
                times = 3
                i += 1
            elif s[i + 1] == "2":
                times = 2
                i += 1
            else:
                times = 1
            self.rotate(face, times)
            i += 1

    def vis(self):
        tmp = '         |'
        for i in range(3):
            print(tmp, end = '')
            for j in range(3):
                print(self.state[self.loc['U']][i, j], end = ' ')
            print('|')
        print('---------+---------+-------------------')
        for i in range(3):
            for j in range(3):
                print(self.state[self.loc['L']][i, j], end = ' ')
            print('|', end='')
            for j in range(3):
                print(self.state[self.loc['F']][i, j], end = ' ')
            print('|', end='')
            for j in range(3):
                print(self.state[self.loc['R']][i, j], end = ' ')
            print('|', end='')
            for j in range(3):
                print(self.state[self.loc['B']][i, j], end = ' ')
            print()
        print('---------+---------+-------------------')
        for i in range(3):
            print(tmp, end = '')
            for j in range(3):
                print(self.state[self.loc['D']][i, j], end = ' ')
            print('|')
        print()
        draw_cube_3D(self.state, self.loc)

if __name__=='__main__':
    cubes = cube()
    # cubes.run("F2 L' U' L2 D F2 D2 B2 U' B2 U' R2 F' R2 B' L' U R D2 F")
    s = input('please input your movements:')
    cubes.run(s)
    cubes.vis()