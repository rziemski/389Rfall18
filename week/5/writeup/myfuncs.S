section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rax, rdi  ;moves first param into rax
		      ;second param will be in rsi
	mov rdi, rdx  ;moves 3rd param into rdx

	mov rcx, 0    ;move 0 to rcx to start for loop at 0

forloop:
	mov rax, rsi  ;moves value in rsi to the string
	add rax, 1    ;increments rax pointer by one
	add rcx, 1    ;increments counter by one
	cmp rcx, rdi  ;see if i < strl, compare registers rcx(i) and rdi(strl)
	jl forloop    ;if rcx < rdi then string not complete loop again
	jge end       ;if i >= strl then end it

end:


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

	mov rax, rsi  ;need to move src to rax to copy string over
	mov rsi, rdi  ;rsi needs to point to the destination
	mov rcx, rdx  ;needs to know how much data to copy
	 	      
	stosb   
		
	
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
