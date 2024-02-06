TITLE MASM Template
; Description:4110056009_HW2-2
;
; Revision date: 
INCLUDE Irvine32.inc
.data
.code
BetterRandomRange PROC
    sub ebx, eax
    xchg ebx, eax
    call RandomRange
    neg ebx
    sub eax, ebx
    call writeint
    call crlf
    ret
BetterRandomRange ENDP
main1 PROC
    mov ecx,50
    l1:
        mov ebx,-300 ; lower bound
        mov eax,100 ; upper bound
        call BetterRandomRange

     loop l1
exit
main1 ENDP

END main1
