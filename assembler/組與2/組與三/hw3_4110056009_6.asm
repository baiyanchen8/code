TITLE MASM Template
; Description:4110056009_HW3-6

;
; Revision date: 
INCLUDE Irvine32.inc
.data
A1 byte "1. x AND y ",0Dh,0Ah,"2. x OR y ",0Dh,0Ah,"3. NOT x ",0Dh,0Ah,"4. x XOR y ",0Dh,0Ah,0;0dh,0ah¸õ¦æ
B1 byte "choose one of menu(it must be a number)",0Dh,0Ah,0;
C1 byte "input hex:x",0Dh,0Ah,0;
D1 byte "input hex:y",0Dh,0Ah,0;
E1 byte "answer hex is ",0;
x dword ?
y dword ?

CaseTable BYTE '1' ; 
DWORD AND_op 
EntrySize = ($ - CaseTable)
BYTE '2'
 DWORD OR_op
 BYTE '3'
 DWORD NOT_op
 BYTE '4'
 DWORD XOR_op
NumberOfEntries = ($ - CaseTable)/EntrySize
.code
    main PROC
        mov ebx, offset Casetable
        mov edx, offset A1
        call writestring
        call readchar
        mov ecx,NumberOfEntries
        l1 :
        cmp al,[ebx]
        jne l2
        add ebx,EntrySize
        call near ptr [ebx+1]
        loop l1
        l2 :
        add ebx,EntrySize
        loop l1
        exit
    main ENDP
    ;------------------------------
    XOR_op PROC
    mov edx,offset C1
    call writestring
    call readhex
    mov x,eax
    mov edx,offset C1
    call writestring
    call readhex
    xor eax,x
    
    mov edx,offset E1
    call writestring
    call writehex
    call crlf
    ret
    XOR_op endp
;---------------------------------
    NOT_op PROC
    mov edx,offset C1
    call writestring
    call readhex
    not eax
    mov edx,offset E1
    call writestring
    call writehex
    call crlf
    ret
    NOT_op endp
    ;------------------------------
    OR_op PROC
    mov edx,offset C1
    call writestring
    call readhex
    mov x,eax
    mov edx,offset D1
    call writestring
    call readhex
    mov y,eax
    mov eax,x
    or eax,y
    mov edx,offset E1
    call writestring
    call writehex
    call crlf
    ret
    OR_op endp
    ;-----------------------------
    AND_op PROC
    mov edx,offset C1
    call writestring
    call readhex
    mov x,eax
    mov edx,offset D1
    call writestring
    call readhex
    mov y,eax
    mov eax,x
    and eax,y
    mov edx,offset E1
    call writestring
    call writehex
    call crlf
    ret
    AND_op endp
  
END main