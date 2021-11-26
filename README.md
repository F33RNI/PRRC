<h1 align="center">Programmable Rainbow Redstone Computer</h1>

<p align="center">
    <img src="LOGO.png" >
</p>

<div style="width:100%;text-align:center;">
    <p align="center">
        <a href="https://twitter.com/fern_hertz"><img alt="Twitter" src="https://img.shields.io/twitter/url?label=My%20twitter&style=social&url=https%3A%2F%2Ftwitter.com%2Ffern_hertz" ></a>
        <a href="https://youtu.be/6nqyTfuWk78"><img src="https://img.shields.io/badge/YouTube-PRRC%20Intro-red" ></a>
        <a href="https://github.com/XxOinvizioNxX/PRRC/stargazers"><img src="https://img.shields.io/github/stars/XxOinvizioNxX/PRRC" ></a>
        <a href="https://github.com/XxOinvizioNxX/PRRC/releases"><img src="https://img.shields.io/badge/download_map-1.12.2-informational?logo=Github&color=purple" ></a>
    </p>
</div>

## Table of contents

- [What is it?](#what-is-it)
- [How to use it](#how-to-use-it)
- [Program flasher](#program-flasher)

----------

## What is it?

PRRC is Programmable Rainbow Redstone Computer. This is my first 8-bit computer built in Minecraft that can be programmed in assembler. The program can be flashed using a Python script that places torches in accordance with the specified bits

Some specs:
- **Clock frequency:** 0.2Hz
- **Registers:** 30 (27 regular registers + 2 I/O + 1 Carry IN/OUT) (expands up to 256)
- **Digital inputs/outputs:** 2 registers x 8 bits = 16
- **Flash size:** 64 commands x 19 bits (expands up to 256 x 19)
- **Assembler commands:** 8 (PUT, MOV, JMP, BRC, NOR, AND, ADD, ADC)

<p align="center">
    <img src="SCREENSHOT.png" >
    <br >
    <img src="STRUCTURE.png" >
</p>

Comparing two numbers in Minecraft using PRRC (YouTube):

[![Comparing two numbers in Minecraft using PRRC](https://img.youtube.com/vi/6nqyTfuWk78/0.jpg)](https://www.youtube.com/watch?v=6nqyTfuWk78)

----------

## How to use it

### Flash memory

The program writes in assembly language. Each command consists of 19 bits
- 3 bits of instruction
  - 0 (0x000) - PUT Rd N  - Write 8-bit number N to the register with 8-bit address Rd
  - 1 (0x001) - MOV Rd Rs - Copy number from register Rs to register Rd
  - 2 (0x010) - JMP Addr. - Jump to the 8-bit Addr. address
  - 3 (0x011) - BRC Addr. - Jump to the 8-bit Addr. address if carry bit is set
  - 4 (0x100) - NOR Rd Rs - Logic NOR operation between Rd and Rs. The result will be written to Rd
  - 5 (0x101) - AND Rd Rs - Logic AND operation between Rd and Rs. The result will be written to Rd
  - 6 (0x110) - ADD Rd Rs - Arithmetic addition of Rd to Rs without carry bit. The result will be written to Rd
  - 7 (0x111) - ADC Rd Rs - Arithmetic addition of Rd to Rs with carry bit. The result will be written to Rd
- 8 bits (1 byte) of first argument. By default connected to the RAM address bus. Can be connected to Program counter register (in JMP or BRC instructions)
- 8 bits (1 byte) of second argument. Can be connected to the data bus or RAM address bus

### Program counter

A register that stores the current instruction address for program memory. After executing commands 0 to 1 and 4 to 7, it adds 1 to the address. The address can be manually assigned using JMP (2) or BRC (3) commands. If no carriage has been set when the BRC command is executed, the current address will be incremented without assignment

### RAM (Registers 1-15 and 17-30)

29 bytes of RAM (registers) are available for program execution.
Register 1 also used for Carry bit. If a carriage return was performed while performing the addition, it will be written as the last bit in the register 1 (0b00000001). When writing, the remaining bits of the register are not affected

### Digital inputs/outputs (Registers 16 and 31)

In the current version of the computer, 2 registers are available as input / output ports (Register 16 (0b00010000) and register 31 (0b00011111)). Each of the two registers has 8 external inputs and 8 external outputs. To read / write digital ports, the same functions are used as for regular registers

For example, to turn on the lamp on the least significant bit of register 31, just execute command `PUT 31 1`

Reading from this registry copies the data from the levers

### NULL register (Register 0)

0 address does not exist and this register cannot be accessed. The 0th register is used exclusively as a buffer when copying from one register to another

### ALU (Arithmetic Logic Unit)

ALU is the heart of the computer. It performs logical and arithmetic operations. The current version supports 3 operations that ALU performs:
- NOR. Logic NOR operation (Not-OR)
- AND. Logic AND operation
- ADD (ADC). Arithmetic addition

### Reset

After setting the reset, the entire computer stops, the contents of the RAM and the instruction decoder are cleared, the 0th address of the program memory is set

### Clock

The current version of PRRC uses 0.2 Hz redtone clock. You can slow it down without any problem, but speeding up can cause problems due to slow redstone transmission

----------

## Program flasher

coming soon...
