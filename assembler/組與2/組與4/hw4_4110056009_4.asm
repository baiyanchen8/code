TITLE MASM Template
; Description:4110056009_HW3-6

;
; Revision date: 
INCLUDE Irvine32.inc
.data
a dword -1,23,3,4,2,3,4,3,3,3,3,3
a1 dword 1,2,3,4,5,6,7,8,9,10
ass dword 1,2,3,3,3,3,3,5
.code
    main PROC
    call clrscr
    push offset a
    mov eax,type a
    push  eax
    mov eax,lengthof a
    push eax
    call FindThrees
    call writeint

    push offset a1
    mov eax,type a1
    push  eax
    mov eax,lengthof a1
    push eax
    call FindThrees
    call writeint

    push offset ass
    mov eax,type ass
    push  eax
    mov eax,lengthof ass
    push eax
    call FindThrees
    call writeint

    main endp

    FindThrees proc
    push ebp
    mov ebp,esp
    mov ecx ,[ebp+8]; ecx => lenthof a
    mov edx ,[ebp+12]; tpye a
    mov esi ,[ebp+16]; offset of a
    mov eax,0

    loop1 :
        mov ebx , [esi] 

        cmp ebx,3
        jne next
        add eax,1
        next:
        
        add esi,edx
    loop loop1

    cmp eax,3
    jae L1
    mov eax,0
    jmp L2
    L1:mov eax,1
    L2:

    pop ebp 
    ret 12
    FindThrees endp
END main