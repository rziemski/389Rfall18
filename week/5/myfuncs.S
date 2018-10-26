section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rax, rdi  ;moves first param from rdi to rax
                      ;rsi will have the second param
        mov rdi, rdx  ;moves 3 param from rdx to rdi

        mov rcx, 0    ;move 0 to rdi to start for loop at 0

forloop:
        mov rax, rsi  ;moves value in rsi to the string
        add rax, 1
        cmp rcx, rdi  ;see if i < strl, compare registers rcx (i) and rdi (strl)
        jl forloop    ;loop again if rcx < rsi
        jge end       ;if i >= strl

end:


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!

global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rax, rdi



        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
