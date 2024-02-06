INCLUDE irvine32.inc

    
   .data 
    BUFMAX = 128 
    key BYTE BUFMAX+1 DUP(0)
    keySize DWORD ?

    mes BYTE BUFMAX+1 DUP(0)
    mesize DWORD ?

    A1   BYTE    "密鑰: ", 0
    A2   BYTE    "訊息:", 0
    A3  BYTE    "加密訊息: ", 0
    A4   BYTE    "原訊息: ", 0
    A5   BYTE    "ASCII code: ", 0
.code
main PROC

    call Input
    call Encrypt
    
    mov EDX, offset A3
    call WriteString
    mov EDX, offset mes
    call WriteString
    call crlf
    mov EDX, offset A5
    call WriteString
    mov ecx,mesize
    mov esi ,0
    mov eax,0
    loop1:
    mov al,[mes+esi]
    inc esi
    call writeint
    loop loop1
    

    call Encrypt
     call crlf
    mov EDX, offset A4
    call WriteString
    mov EDX, offset mes
    call WriteString
    call crlf
    mov EDX, offset A5
    call WriteString
    mov ecx,mesize
    mov esi ,0
    mov eax,0
    loop2:
    mov al,[mes+esi]
    inc esi
    call writeint
    loop loop2
    
    call crlf
exit


main ENDP


Input PROC
                 

mov EDX, offset A1   
call WriteString
mov ECX, BUFMAX       
mov EDX, offset key        
call ReadString           
mov keySize, EAX          


    mov EDX, offset A5
    call WriteString
    mov ecx,keySize
    mov esi ,0
    mov eax,0
    loop1:
    mov al,[key+esi]
    inc esi
    call writeint
    loop loop1
    call crlf

mov EDX, offset A2       
call WriteString
mov ECX, BUFMAX             
mov EDX, offset mes         
call ReadString             
mov mesize, EAX           
call Crlf

ret

Input ENDP

Encrypt PROC

mov ECX, mesize            
mov ESI, 0  
mov EAX, 0                  

L1:
mov AL, key[EAX]
xor mes[ESI], AL        
inc ESI 
inc EAX
cmp keySize, EAX
jb below
loop L1
below:
mov EAX, 0
loop L1
call crlf
ret

Encrypt ENDP

END main