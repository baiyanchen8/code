TITLE MASM Template
; Description:4110056009_HW3-2
;
; Revision date: 
INCLUDE Irvine32.inc
.data
N=10

array SDWORD N DUP(-10,-8,-6,-4,-2,-1,1,3,5,7)
j DWORD ?
k DWORD ?
tmp sword ?
.code
    main PROC
        call Clrscr
        mov j, 0; you can change the value to change range
        mov k, 11; you can change the value to change range
        

        mov ESI, OFFSET array
        mov ECX, N
        call SummingArrayElementsInRange
        call WriteInt
        call crlf

        mov j, -11; you can change the value to change range
        mov k, 0; you can change the value to change range
        mov ESI, OFFSET array
        mov ECX, N
        call SummingArrayElementsInRange
        call WriteInt
        call crlf
      
        exit
    main ENDP

    SummingArrayElementsInRange PROC
        push ecx
        push esi
        mov eax, 0

        l1:
            mov ebx, [esi]
            cmp j,ebx
            jle t1;有號數比較跳轉j>=ebx
            jmp next
            t1:
                cmp ebx, k;比較
                jle t2;有號數比較跳轉ebx>=k
                jmp next
            t2:
                add eax, ebx
            next:
                add esi, 4

        loop l1
        call crlf
        pop esi
        pop ecx
        ret
    SummingArrayElementsInRange ENDP

END main