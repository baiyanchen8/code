TITLE MASM Template
; Description:4110056009_HW2-2
;
; Revision date: 
INCLUDE Irvine32.inc
.data
start dword 1
chars byte 'H','A','C','E','B','D','F','G'
links dword  0,4,5,6,2,3,7,0

.code

main1 PROC
    mov ecx,lengthof links
    mov edi,offset links
    mov edx,1
    mov esi ,OFFSET chars
    mov eax,0
    l1:
        mov ebx,start
       mov al,byte ptr [esi+ebx]
       call writechar
       mov ebx,start
       mov eax,dword ptr [edi+ebx*4]
       mov start,eax
    loop l1
       



exit
main1 ENDP

END main1
