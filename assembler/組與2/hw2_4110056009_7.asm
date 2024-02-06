TITLE MASM Template
; Description:4110056009_HW2-2
;
; Revision date: 
INCLUDE Irvine32.inc
.data
rows WORD 50
cols WORD 50


.code
    main PROC
        call Clrscr
        mov ecx, 100
        L1:
            call GetMaxXY
            mov rows, ax
            mov cols, dx
          
            movzx eax, rows
            call RandomRange
            mov dh, al

            movzx eax, cols
            call RandomRange
            mov dl, al

            call Gotoxy        ; locate cursor

            mov al,'H'
            call WriteChar

            mov eax,100
            call Delay

        Loop L1

        exit
    main ENDP

END main
