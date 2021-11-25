"""
 Copyright (C) 2021 Fern H. , PRRC Uploader

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 See the License for the specific language governing permissions and
 limitations under the License.

 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR
 OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
"""

#####################################
#            The program            #
#####################################

# Place your program code here in 2D int list (bits) or 1D string list. Each line per one instruction.
# Format: [[bit 0, bit 1, ..., bit n], [...]] OR ['COMMAND 1st_argument(DEC) 2nd_argument(DEC)', '.. .. ..']
# Examples:
# INSTRUCTIONS = [[0, 0, 0,   0, 0, 0, 0, 0, 0, 1, 1,   1, 0, 1, 0, 1, 0, 1, 0],  # 0
#                 [0, 0, 1,   0, 0, 0, 1, 1, 1, 1, 1,   0, 0, 0, 0, 0, 0, 1, 1]]  # 1
# OR
# INSTRUCTIONS = ['PUT 3 170',  # 0
#                 'MOV 31 3']   # 1


# A program for comparing two numbers with each other (register 16 with register 31).
# The answer is written into register 31 (1 - the first number is greater, 2 - the second, 3 - the numbers are equal).
INSTRUCTIONS = ['MOV 2 31',     # 0 - Copy digital input register 31 (2nd number) to the register 2
                'NOR 2 2',      # 1 - Invert value in register 2 (invert 2nd number)
                'ADD 2 16',     # 2 - Add 1st number (digital input register 16) to the register 2
                'BRC 5',        # 3 - Goto 5 if carry is set (1st number > 2nd number)
                'JMP 7',        # 4 - Goto 7 (skip 5, 6) if no carry (1st number <= 2nd number)
                'PUT 31 1',     # 5 - Light up first lamp on digital output (register 31) (1st number > 2nd number)
                'JMP 14',       # 6 - Goto 14 to finish the program
                'PUT 3 1',      # 7 - Write 1 to register 3 (for next addition)
                'ADD 2 3',      # 8 - Add 1 to previous result (if a carry appears, the numbers are equal)
                'BRC 11',       # 9 - Goto 11 if carry is set (1st number == 2nd number)
                'JMP 13',       # 10 - Goto 13 (skip 11, 12) if no carry (1st number < 2nd number)
                'PUT 31 3',     # 11 - Light up both lamps on digital output (register 31) (1st number = 2nd number)
                'JMP 14',       # 12 - Goto 14 to finish the program
                'PUT 31 2',     # 13 - Light up second lamp on digital output (register 31) (1st number < 2nd number)
                'JMP 14'        # 14 - Goto 14 to make infinite loop
                ]

"""
# A program for integer division between 8-bit numbers (register 16 divide by 31).
# The answer is written into register 31
INSTRUCTIONS = ['PUT 2 1',      # 0 - 1 (0b00000001) constant
                'MOV 3 16',     # 1 - Copy 1st number (from digital input register 16)
                'MOV 4 31',     # 2 - Copy 2nd number (from digital input register 31)
                'NOR 4 4',      # 3 - Invert value in register 4 (invert 2nd number to make subtraction for loop)
                'ADD 5 2',      # 4 - Increment answer by 1
                'ADD 3 4',      # 5 - Subtract 2nd number from previous result
                'BRC 8',        # 6 - Continue loop if no carry
                'JMP 10',       # 7 - Exit from loop and write the answer
                'ADD 3 2',      # 8 - Add 1 (from register 2) to complete subtraction
                'JMP 4',        # 9 - Another loop entry
                'MOV 16 5',     # 10 - Copy answer to the digital output (register 16)
                'JMP 11'        # 11 - Goto 11 to make infinite loop
                ]
"""


"""
# A program that switches sequentially the lamps in the output register
INSTRUCTIONS = ['PUT 1 1',
                'ADC 2 2',
                'MOV 16 2',
                'JMP 1'
                ]
"""


################################
#            Config            #
################################

# Dictionary of available commands
# By default there are 8 commands:
# 0 (0x000) - PUT Rd N  - Write 8-bit number N to the register with 8-bit address Rd
# 1 (0x001) - MOV Rd Rs - Copy number from register Rs to register Rd
# 2 (0x010) - JMP Addr. - Jump to the 8-bit Addr. address
# 3 (0x011) - BRC Addr. - Jump to the 8-bit Addr. address if carry bit is set
# 4 (0x100) - NOR Rd Rs - Logic NOR operation between Rd and Rs. The result will be written to Rd
# 5 (0x101) - AND Rd Rs - Logic AND operation between Rd and Rs. The result will be written to Rd
# 6 (0x110) - ADD Rd Rs - Arithmetic addition of Rd to Rs without carry bit. The result will be written to Rd
# 7 (0x111) - NOR Rd Rs - Arithmetic addition of Rd to Rs with carry bit. The result will be written to Rd
# If you downloaded the original map, do not change it!
# Do not change if you are not sure what you are doing!
DICTIONARY = [['PUT', [0, 0, 0]],
              ['MOV', [0, 0, 1]],
              ['JMP', [0, 1, 0]],
              ['BRC', [0, 1, 1]],
              ['NOR', [1, 0, 0]],
              ['AND', [1, 0, 1]],
              ['ADD', [1, 1, 0]],
              ['ADC', [1, 1, 1]]]

# Maximum number of characters in one command block
# Do not change if you are not sure what you are doing!
# By default - 32000
COMMAND_BLOCK_CHARS_LIMIT = 32000

# Redstone torches facing
# BE CAREFUL! FACING IS NOT THE FACING OF THE PLAYER, but the facing of the torches.
# You can see this value in F3 by hovering over the torch (bottom right: minecraft: redstone_torch, facing: FACING).
# Warning! Tested only with west facing
# If you downloaded the original map, do not change it. By default - west
BITS_TORCHES_FACING = 'west'

# Layers with data bits. Specify in the format
# [X coordinate of the first torch, Y coordinate of the first torch, Z coordinate of the first torch,
# number of lines (instructions in a layer)].
# If you downloaded the original map, do not change it. By default - [[-290, 66, -724, 32], [-290, 72, -724, 32]]
LAYERS = [[-289, 66, -724, 32],
          [-289, 71, -724, 32]]

# Command header (first part) in command block (regardless of part).
# Removes the redstone block before the current command block and summons activating rails above the redstone block.
# Do not change if you are not sure what you are doing!
COMMAND_HEADER = "summon falling_block ~0 ~1 ~0 {Block:leaves,Time:1,Passengers:[{id:falling_block," \
                 "Block:redstone_block,Time:1,Passengers:[{id:falling_block,Block:activator_rail,Time:1," \
                 "Passengers:[" \
                 "{id:commandblock_minecart,Command:\"fill ~-1 ~-3 ~ ~-1 ~-3 ~ air\"},"

# End of command in command block (regardless of part).
# Removes all blocks from above and kills minecarts.
# Do not change if you are not sure what you are doing!
COMMAND_FOOTER = "{id:commandblock_minecart,Command:\"fill ~ ~1 ~ ~ ~1 ~ leaves\"}," \
                 "{id:commandblock_minecart,Command:\"summon falling_block ~ ~2 ~ " \
                 "{Block:command_block,Time:1,TileEntityData:{Command:\\\"fill ~ ~-4 ~ ~ ~1 ~ air\\\"}," \
                 "Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}\"}," \
                 "{id:commandblock_minecart,Command:\"kill @e[type=commandblock_minecart]\"}]}]}]}"

# Command that prohibits / allows output of service information of command blocks. By default - false.
# Do not change if you are not sure what you are doing!
GAMERULE_COMMAND = "{id:commandblock_minecart,Command:\"gamerule commandBlockOutput false\"},"

# Number of torches (bits) in one line (instructions)
# If you downloaded the original map, do not change it! By default - 3 + 8 + 8 = 19
TORCHES_IN_LINE = 19


######################################################
#            Things are getting deeper...            #
######################################################


def parse_instruction(instructions_list):
    """
    Parsed 1D list of strings instructions into 2D array of bit instructions using DICTIONARY
    :param instructions_list: 1D String list of instructions ['instruction 0', 'instruction 1']
    :return: 2D list of instructions [[0, 0, ...], [...]]
    """
    parsed_instructions = []
    for instruction_str in instructions_list:
        # Found current command in dictionary
        instruction = []
        for parsed_command in DICTIONARY:
            if instruction_str.startswith(parsed_command[0]):
                instruction = parsed_command[1].copy()

        # Check if command exists
        if len(instruction) == 0:
            print('ERROR! No commands for instruction ' + instruction_str + ' were found in the dictionary!')
            exit(0)
            return [[]]

        # Split by space
        instructions_str = instruction_str.strip().split(' ')

        # Extract 8 bit arguments from string
        argument_1_str = '00000000'
        argument_2_str = '00000000'
        if len(instructions_str) > 0:
            if len(instructions_str) > 1:
                argument_1_str = format(int(instructions_str[1]), '08b')
            if len(instructions_str) > 2:
                argument_2_str = format(int(instructions_str[2]), '08b')

        # Build entire instruction with provided bits
        for argument_1_bit in argument_1_str:
            if argument_1_bit != '0':
                instruction.append(1)
            else:
                instruction.append(0)
        for argument_2_bit in argument_2_str:
            if argument_2_bit != '0':
                instruction.append(1)
            else:
                instruction.append(0)

        # Append current instruction to list
        parsed_instructions.append(instruction)
    return parsed_instructions


def get_next_bit(bit_x: int, bit_y: int, bit_z: int):
    """
    Calculates next position of torch in one line
    Be careful! facing is not the facing of the player, but the facing of the torches.
    You can see this value in F3 by hovering over the torch (bottom right: minecraft: redstone_torch, facing: FACING)
    Warning! Tested only with BITS_TORCHES_FACING = 'west'
    :param bit_x: current torch X position
    :param bit_y: current torch Y position
    :param bit_z: current torch Z position
    :return: next torch position (X, Y, Z)
    """
    if BITS_TORCHES_FACING == 'north':
        bit_x -= 2
    elif BITS_TORCHES_FACING == 'east':
        bit_z -= 2
    elif BITS_TORCHES_FACING == 'south':
        bit_x += 2
    elif BITS_TORCHES_FACING == 'west':
        bit_z += 2

    return bit_x, bit_y, bit_z


def get_next_line_layer(start_bit_x: int, start_bit_y: int, start_bit_z: int, layer_index: int):
    """
    Calculates starting position of the next line (including a new layer)
    Warning! Tested only with BITS_TORCHES_FACING = 'west'
    :param start_bit_x: start torch X position on current line
    :param start_bit_y: start torch Y position on current line
    :param start_bit_z: start torch Z position on current line
    :param layer_index: current layer index (0 - first layer)
    :return: next line start torch position (X, Y, Z)
    """
    if BITS_TORCHES_FACING == 'north':
        start_bit_z += 2
        # Start new layer on current layer ending
        if start_bit_z >= LAYERS[layer_index][2] + LAYERS[layer_index][3] * 2:
            layer_index += 1
            if layer_index >= len(LAYERS):
                print('ERROR! Overflow! Not enough layers!')
                exit(0)
            return LAYERS[layer_index][0], LAYERS[layer_index][1], LAYERS[layer_index][2], layer_index
    elif BITS_TORCHES_FACING == 'east':
        start_bit_x -= 2
        # Start new layer on current layer ending
        if start_bit_x <= LAYERS[layer_index][0] - LAYERS[layer_index][3] * 2:
            layer_index += 1
            if layer_index >= len(LAYERS):
                print('ERROR! Overflow! Not enough layers!')
                exit(0)
            return LAYERS[layer_index][0], LAYERS[layer_index][1], LAYERS[layer_index][2], layer_index
    elif BITS_TORCHES_FACING == 'south':
        start_bit_z -= 2
        # Start new layer on current layer ending
        if start_bit_z >= LAYERS[layer_index][2] - LAYERS[layer_index][3] * 2:
            layer_index += 1
            if layer_index >= len(LAYERS):
                print('ERROR! Overflow! Not enough layers!')
                exit(0)
            return LAYERS[layer_index][0], LAYERS[layer_index][1], LAYERS[layer_index][2], layer_index
    elif BITS_TORCHES_FACING == 'west':
        start_bit_x += 2
        # Start new layer on current layer ending
        if start_bit_x >= LAYERS[layer_index][0] + LAYERS[layer_index][3] * 2:
            layer_index += 1
            if layer_index >= len(LAYERS):
                print('ERROR! Overflow! Not enough layers!')
                exit(0)
            return LAYERS[layer_index][0], LAYERS[layer_index][1], LAYERS[layer_index][2], layer_index

    return start_bit_x, start_bit_y, start_bit_z, layer_index


def erase_all_commands(command: str):
    """
    Erases (removes) all torches (bits) on all layers
    :param command: current command (String)
    :return: command (String)
    """
    command += "{id:commandblock_minecart,Command:\"say Erasing memory...\"},"
    for layer in LAYERS:
        # Calculate first and last torch position on current layer
        first_position = str(layer[0]) + " " + str(layer[1]) + " " + str(layer[2])
        last_bit_in_line_x = layer[0]
        last_bit_in_line_y = layer[1]
        last_bit_in_line_z = layer[2]
        for _ in range(TORCHES_IN_LINE):
            last_bit_in_line_x, last_bit_in_line_y, last_bit_in_line_z = \
                get_next_bit(last_bit_in_line_x, last_bit_in_line_y, last_bit_in_line_z)
        if BITS_TORCHES_FACING == 'north':
            last_bit_in_line_z += (layer[3] - 1) * 2
        elif BITS_TORCHES_FACING == 'east':
            last_bit_in_line_x -= (layer[3] - 1) * 2
        elif BITS_TORCHES_FACING == 'south':
            last_bit_in_line_z -= (layer[3] - 1) * 2
        elif BITS_TORCHES_FACING == 'west':
            last_bit_in_line_x += (layer[3] - 1) * 2
        last_position = str(last_bit_in_line_x) + " " + str(last_bit_in_line_y) + " " + str(last_bit_in_line_z)

        # Replace all redstone torches on current layer with air
        command += "{id:commandblock_minecart,Command:\"fill " + first_position + " " + last_position \
                   + " air 0 replace redstone_torch\"},"
        command += "{id:commandblock_minecart,Command:\"fill " + first_position + " " + last_position \
                   + " air 0 replace unlit_redstone_torch\"},"

    command += "{id:commandblock_minecart,Command:\"say Erasing done. Writing program...\"},"
    return command


def start_new_command_block(command: str):
    """
    Displays a message about the end of the current part and the beginning of a new one.
    Also places a redstone block at the next command block.
    :param command: current command (String)
    :return: command (String)
    """
    command += "{id:commandblock_minecart,Command:\"say Part " + str(current_part) + " done! Starting part " \
               + str(current_part + 1) + "\"}," \
                                         "{id:commandblock_minecart,Command:\"fill ~2 ~-3 ~ ~2 ~-3 ~ redstone_block\"},"
    return command


# Main program entry point
if __name__ == "__main__":
    instructions = []
    # Check if instruction is empty or in String or BIN format
    if len(INSTRUCTIONS) == 0:
        # Empty
        instructions = []
    elif isinstance(INSTRUCTIONS[0], list):
        # BIN format
        instructions = INSTRUCTIONS.copy()
    else:
        # Parse instruction from string
        instructions = parse_instruction(INSTRUCTIONS).copy()

    # Print entire program to the console
    print('Program (' + str(len(instructions)) + ' instructions):')
    for i in range(len(instructions)):
        print(str(i) + ': ' + str(instructions[i]))

    # Check length of instruction
    for i in range(len(instructions)):
        if len(instructions[i]) != TORCHES_IN_LINE:
            print('ERROR! The number of bits (' + str(len(instructions[i])) + ') on line with index '
                  + str(i) + ' (' + str(bin(i)) + ') does not match the specified number of torches in one line ('
                  + str(TORCHES_IN_LINE) + ')')
            print(instructions[i])
            exit(0)

    # Current command block number
    current_part = 0

    # Current layer index
    current_layer = 0

    # Start new command with header
    current_command = COMMAND_HEADER + GAMERULE_COMMAND

    # Erase memory
    current_command = erase_all_commands(current_command)

    # Get start program position
    line_start_x = LAYERS[0][0]
    line_start_y = LAYERS[0][1]
    line_start_z = LAYERS[0][2]

    for i in range(len(instructions)):
        current_x, current_y, current_z = line_start_x, line_start_y, line_start_z

        for bit in instructions[i]:
            # Build current torch position into string
            coordinates_string = str(current_x) + " " + str(current_y) + " " + str(current_z)

            # Set bit (or start new part)
            if int(bit) > 0:
                # Test length with new bit
                current_command_temp = start_new_command_block(current_command
                                                               + "{id:commandblock_minecart,Command:\"setblock "
                                                               + coordinates_string + " redstone_torch facing="
                                                               + BITS_TORCHES_FACING + "\"},")
                current_command_temp += COMMAND_FOOTER

                # If the limit has reached
                if len(current_command_temp) > COMMAND_BLOCK_CHARS_LIMIT:
                    # Output current command
                    print()
                    print('PART ' + str(current_part + 1) + '. Place the text below in the ' +
                          str(current_part + 1) + ' command block')
                    print()
                    print(start_new_command_block(current_command) + COMMAND_FOOTER)
                    print()

                    # Start new part
                    current_part += 1
                    current_command = COMMAND_HEADER + GAMERULE_COMMAND

                # Set bit
                current_command += "{id:commandblock_minecart,Command:\"setblock " \
                                   + coordinates_string + " redstone_torch facing=" + BITS_TORCHES_FACING + "\"},"

            # Update position
            current_x, current_y, current_z = get_next_bit(current_x, current_y, current_z)

        # Switch to new line
        if i < len(instructions) - 1:
            line_start_x, line_start_y, line_start_z, current_layer = \
                get_next_line_layer(line_start_x, line_start_y, line_start_z, current_layer)

    # Ending of command
    current_command += "{id:commandblock_minecart,Command:\"say Writing done!\"},"
    current_command += COMMAND_FOOTER

    # Print command
    print()
    print('PART ' + str(current_part + 1) + '. Place the text below into the ' +
          str(current_part + 1) + ' command block')
    print()
    print(current_command)
    print()
