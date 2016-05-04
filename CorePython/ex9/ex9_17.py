# !/usr/bin/env python
# -*- coding: utf-8 -*-


def menu():
    title1 = ''.join([10 * '#', 'MENU', 10 * '#'])
    prompt1 = '''Please choose the function:
(C)reat a file;
(S)how a file;
(E)dit a file;
(Q)uit
'''
    while True:
        print title1
        print prompt1
        choice = raw_input('> ')[0].lower()
        if choice == 'q':
            break
        elif choice not in 'ces':
            print "Illegal choice! Try again!"
        elif choice == 'c':
            create_file()
        elif choice == 's':
            show_file()
        else:
            edit_file()


def create_file():
    title1 = ''.join([10 * '*', 'create a file', 10 * '*'])
    print title1
    file_name = raw_input("File name:\n> ")

    print 30 * '-'
    tmp_txt = []
    while True:
        line = raw_input()
        if line == 'EOF':  # todo: instead it by a real 'EOF'
            break
        line = ''.join([line, '\n'])
        tmp_txt.append(line)
    print "The directory you want to save:"
    print r"(for example: C:\Programs\CorePython\ex9\tmp)"
    directory = raw_input('> ')
    path = ''.join([directory, r'\\'[:-1], file_name, '.txt'])
    new_file = open(path, 'w')
    prompt1 = ''.join(["Creating the file...\n(", path, ')'])
    print prompt1
    new_file.writelines(tmp_txt)
    print "Writing..."
    new_file.close()
    print "Saving...\nFinish!"




def show_file():
    title1 = ''.join([10 * '*', 'show a file', 10 * '*'])
    print title1
    print "Enter the path of file you want to read."
    print r"(for example: C:\Programs\CorePython\ex9\tmp\a.txt)"
    file_path = raw_input('> ')
    file = open(file_path, 'r')
    print "Opening..."
    print 30 * '-'
    line_number = 0
    for eachLine in file:
        line_number += 1
        print "%d\t%s" % (line_number, eachLine),
    file.close()
    print 30 * '-'


def edit_file():
    title1 = ''.join([10 * '*', 'edit a file', 10 * '*'])
    print title1
    print "Enter the path of file you want to edit."
    print r"(for example: C:\Programs\CorePython\ex9\tmp\a.txt)"
    file_path = raw_input('> ')
    e_file = open(file_path, 'r')
    print "Opening..."
    print 30 * '-'
    all_lines = e_file.readlines()
    e_file.close()
    line_number = 0
    for eachLine in all_lines:
        line_number += 1
        print "%d\t%s" % (line_number, eachLine),
    print 30 * '-'
    while True:
        edit_line = raw_input("Which line do you want to edit?\n> ")
        try:
            edit_line = int(edit_line)
            if 0 < edit_line <= len(all_lines):
                break
            else:
                print "Illegal line number! Try again!"
        except ValueError:
            print "Not a number! Try again!"
    new_line = raw_input("Please enter the new line:\n> ")
    all_lines[edit_line - 1] = ''.join([new_line, '\n'])
    e_file = open(file_path, 'w')
    e_file.writelines(all_lines)
    print "Writing..."
    e_file.close()
    print "Finish!\nClosing..."


if __name__ == '__main__':
    menu()
