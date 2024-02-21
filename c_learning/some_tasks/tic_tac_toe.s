	.text
	.def	@feat.00;
	.scl	3;
	.type	0;
	.endef
	.globl	@feat.00
.set @feat.00, 0
	.file	"tic_tac_toe.c"
	.def	sprintf;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,sprintf
	.globl	sprintf                         # -- Begin function sprintf
	.p2align	4, 0x90
sprintf:                                # @sprintf
.seh_proc sprintf
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movq	%r9, 104(%rsp)
	movq	%r8, 96(%rsp)
	movq	%rdx, 64(%rsp)
	movq	%rcx, 56(%rsp)
	leaq	96(%rsp), %rax
	movq	%rax, 40(%rsp)
	movq	40(%rsp), %r9
	movq	64(%rsp), %rdx
	movq	56(%rsp), %rcx
	xorl	%eax, %eax
	movl	%eax, %r8d
	callq	_vsprintf_l
	movl	%eax, 52(%rsp)
	movl	52(%rsp), %eax
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	vsprintf;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,vsprintf
	.globl	vsprintf                        # -- Begin function vsprintf
	.p2align	4, 0x90
vsprintf:                               # @vsprintf
.seh_proc vsprintf
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movq	%r8, 64(%rsp)
	movq	%rdx, 56(%rsp)
	movq	%rcx, 48(%rsp)
	movq	64(%rsp), %rax
	movq	56(%rsp), %r8
	movq	48(%rsp), %rcx
	movq	$-1, %rdx
	xorl	%r9d, %r9d
                                        # kill: def $r9 killed $r9d
	movq	%rax, 32(%rsp)
	callq	_vsnprintf_l
	nop
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	_snprintf;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,_snprintf
	.globl	_snprintf                       # -- Begin function _snprintf
	.p2align	4, 0x90
_snprintf:                              # @_snprintf
.seh_proc _snprintf
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movq	%r9, 104(%rsp)
	movq	%r8, 64(%rsp)
	movq	%rdx, 56(%rsp)
	movq	%rcx, 48(%rsp)
	leaq	104(%rsp), %rax
	movq	%rax, 32(%rsp)
	movq	32(%rsp), %r9
	movq	64(%rsp), %r8
	movq	56(%rsp), %rdx
	movq	48(%rsp), %rcx
	callq	_vsnprintf
	movl	%eax, 44(%rsp)
	movl	44(%rsp), %eax
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	_vsnprintf;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,_vsnprintf
	.globl	_vsnprintf                      # -- Begin function _vsnprintf
	.p2align	4, 0x90
_vsnprintf:                             # @_vsnprintf
.seh_proc _vsnprintf
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movq	%r9, 64(%rsp)
	movq	%r8, 56(%rsp)
	movq	%rdx, 48(%rsp)
	movq	%rcx, 40(%rsp)
	movq	64(%rsp), %rax
	movq	56(%rsp), %r8
	movq	48(%rsp), %rdx
	movq	40(%rsp), %rcx
	xorl	%r9d, %r9d
                                        # kill: def $r9 killed $r9d
	movq	%rax, 32(%rsp)
	callq	_vsnprintf_l
	nop
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	main;
	.scl	2;
	.type	32;
	.endef
	.text
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
main:                                   # @main
.seh_proc main
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movl	$0, 68(%rsp)
	movb	$88, 59(%rsp)
	movl	$32, %ecx
	movl	$3, %edx
	leaq	field(%rip), %r8
	callq	init_field
.LBB4_1:                                # =>This Loop Header: Depth=1
                                        #     Child Loop BB4_3 Depth 2
	movl	$3, %ecx
	leaq	field(%rip), %rdx
	callq	victory_check
	movl	%eax, 64(%rsp)
	cmpl	$32, %eax
	jne	.LBB4_12
# %bb.2:                                #   in Loop: Header=BB4_1 Depth=1
	movl	$3, %ecx
	leaq	field(%rip), %rdx
	callq	drow_field
	movsbl	59(%rsp), %edx
	leaq	"??_C@_0CK@KBKEEGHN@?$CFc?5step?0?5enter?5pos?$CInumber?5from?50@"(%rip), %rcx
	movl	$8, %r8d
	callq	printf
.LBB4_3:                                #   Parent Loop BB4_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	leaq	60(%rsp), %rcx
	callq	get_num
	cmpl	$0, 60(%rsp)
	jl	.LBB4_5
# %bb.4:                                #   in Loop: Header=BB4_3 Depth=2
	cmpl	$8, 60(%rsp)
	jle	.LBB4_6
.LBB4_5:                                #   in Loop: Header=BB4_3 Depth=2
	leaq	"??_C@_0P@NNHNHGBC@out?5of?5range?0?5?$AA@"(%rip), %rcx
	callq	printf
	jmp	.LBB4_10
.LBB4_6:                                #   in Loop: Header=BB4_3 Depth=2
	movl	60(%rsp), %eax
	movl	$3, %ecx
	cltd
	idivl	%ecx
	movslq	%eax, %rcx
	leaq	field(%rip), %rax
	imulq	$3, %rcx, %rcx
	addq	%rcx, %rax
	movq	%rax, 48(%rsp)                  # 8-byte Spill
	movl	60(%rsp), %eax
	movl	$3, %ecx
	cltd
	idivl	%ecx
	movq	48(%rsp), %rax                  # 8-byte Reload
	movslq	%edx, %rcx
	movsbl	(%rax,%rcx), %eax
	cmpl	$32, %eax
	je	.LBB4_8
# %bb.7:                                #   in Loop: Header=BB4_3 Depth=2
	leaq	"??_C@_0BD@NJLHBFAJ@cell?5is?5occupied?0?5?$AA@"(%rip), %rcx
	callq	printf
	jmp	.LBB4_9
.LBB4_8:                                #   in Loop: Header=BB4_1 Depth=1
	jmp	.LBB4_11
.LBB4_9:                                #   in Loop: Header=BB4_3 Depth=2
	jmp	.LBB4_10
.LBB4_10:                               #   in Loop: Header=BB4_3 Depth=2
	leaq	"??_C@_0M@OPNOJLIB@try?5again?3?5?$AA@"(%rip), %rcx
	callq	printf
	jmp	.LBB4_3
.LBB4_11:                               #   in Loop: Header=BB4_1 Depth=1
	movb	59(%rsp), %al
	movb	%al, 47(%rsp)                   # 1-byte Spill
	movl	60(%rsp), %eax
	movl	$3, %ecx
	cltd
	idivl	%ecx
	movslq	%eax, %rcx
	leaq	field(%rip), %rax
	imulq	$3, %rcx, %rcx
	addq	%rcx, %rax
	movq	%rax, 32(%rsp)                  # 8-byte Spill
	movl	60(%rsp), %eax
	movl	$3, %ecx
	cltd
	idivl	%ecx
	movq	32(%rsp), %rax                  # 8-byte Reload
	movl	%edx, %ecx
	movb	47(%rsp), %dl                   # 1-byte Reload
	movslq	%ecx, %rcx
	movb	%dl, (%rax,%rcx)
	movsbl	59(%rsp), %edx
	movl	$88, %eax
	movl	$79, %ecx
	cmpl	$88, %edx
	cmovel	%ecx, %eax
                                        # kill: def $al killed $al killed $eax
	movb	%al, 59(%rsp)
	jmp	.LBB4_1
.LBB4_12:
	movl	$3, %ecx
	leaq	field(%rip), %rdx
	callq	drow_field
	cmpl	$32, 64(%rsp)
	je	.LBB4_14
# %bb.13:
	movl	64(%rsp), %edx
	leaq	"??_C@_08NKNFNOFB@?$CFc?5win?$CB?6?$AA@"(%rip), %rcx
	callq	printf
	jmp	.LBB4_15
.LBB4_14:
	leaq	"??_C@_08CCICKHPI@nobody?8s?$AA@"(%rip), %rcx
	callq	printf
.LBB4_15:
	xorl	%eax, %eax
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	init_field;
	.scl	2;
	.type	32;
	.endef
	.globl	init_field                      # -- Begin function init_field
	.p2align	4, 0x90
init_field:                             # @init_field
.seh_proc init_field
# %bb.0:
	subq	$32, %rsp
	.seh_stackalloc 32
	.seh_endprologue
	movq	%r8, 24(%rsp)
	movl	%edx, 20(%rsp)
	movb	%cl, 19(%rsp)
	movl	20(%rsp), %eax
                                        # kill: def $rax killed $eax
	movq	%rax, (%rsp)                    # 8-byte Spill
	movl	$0, 8(%rsp)
.LBB5_1:                                # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_3 Depth 2
	movl	8(%rsp), %eax
	cmpl	20(%rsp), %eax
	jge	.LBB5_8
# %bb.2:                                #   in Loop: Header=BB5_1 Depth=1
	movl	$0, 12(%rsp)
.LBB5_3:                                #   Parent Loop BB5_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	12(%rsp), %eax
	cmpl	20(%rsp), %eax
	jge	.LBB5_6
# %bb.4:                                #   in Loop: Header=BB5_3 Depth=2
	movq	(%rsp), %r8                     # 8-byte Reload
	movb	19(%rsp), %dl
	movq	24(%rsp), %rax
	movslq	8(%rsp), %rcx
	imulq	%r8, %rcx
	addq	%rcx, %rax
	movslq	12(%rsp), %rcx
	movb	%dl, (%rax,%rcx)
# %bb.5:                                #   in Loop: Header=BB5_3 Depth=2
	movl	12(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 12(%rsp)
	jmp	.LBB5_3
.LBB5_6:                                #   in Loop: Header=BB5_1 Depth=1
	jmp	.LBB5_7
.LBB5_7:                                #   in Loop: Header=BB5_1 Depth=1
	movl	8(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 8(%rsp)
	jmp	.LBB5_1
.LBB5_8:
	addq	$32, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	victory_check;
	.scl	2;
	.type	32;
	.endef
	.globl	victory_check                   # -- Begin function victory_check
	.p2align	4, 0x90
victory_check:                          # @victory_check
.seh_proc victory_check
# %bb.0:
	subq	$40, %rsp
	.seh_stackalloc 40
	.seh_endprologue
	movq	%rdx, 24(%rsp)
	movl	%ecx, 20(%rsp)
	movl	20(%rsp), %eax
                                        # kill: def $rax killed $eax
	movq	%rax, (%rsp)                    # 8-byte Spill
	movl	$1, 16(%rsp)
.LBB6_1:                                # =>This Inner Loop Header: Depth=1
	movl	16(%rsp), %eax
	cmpl	20(%rsp), %eax
	jge	.LBB6_6
# %bb.2:                                #   in Loop: Header=BB6_1 Depth=1
	movq	(%rsp), %r8                     # 8-byte Reload
	movq	24(%rsp), %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	imulq	%r8, %rcx
	addq	%rcx, %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movsbl	(%rax,%rcx), %eax
	movq	24(%rsp), %rcx
	movslq	16(%rsp), %rdx
	imulq	%r8, %rdx
	addq	%rdx, %rcx
	movslq	16(%rsp), %rdx
	movsbl	(%rcx,%rdx), %ecx
	cmpl	%ecx, %eax
	je	.LBB6_4
# %bb.3:
	jmp	.LBB6_6
.LBB6_4:                                #   in Loop: Header=BB6_1 Depth=1
	jmp	.LBB6_5
.LBB6_5:                                #   in Loop: Header=BB6_1 Depth=1
	movl	16(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 16(%rsp)
	jmp	.LBB6_1
.LBB6_6:
	movl	16(%rsp), %eax
	cmpl	20(%rsp), %eax
	jne	.LBB6_9
# %bb.7:
	movq	(%rsp), %rdx                    # 8-byte Reload
	movq	24(%rsp), %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movsbl	(%rax,%rcx), %eax
	cmpl	$32, %eax
	je	.LBB6_9
# %bb.8:
	movq	(%rsp), %rdx                    # 8-byte Reload
	movq	24(%rsp), %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movsbl	(%rax,%rcx), %eax
	movl	%eax, 36(%rsp)
	jmp	.LBB6_45
.LBB6_9:
	movl	20(%rsp), %eax
	subl	$1, %eax
	movl	%eax, 16(%rsp)
.LBB6_10:                               # =>This Inner Loop Header: Depth=1
	cmpl	$0, 16(%rsp)
	jle	.LBB6_15
# %bb.11:                               #   in Loop: Header=BB6_10 Depth=1
	movq	(%rsp), %r8                     # 8-byte Reload
	movq	24(%rsp), %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	imulq	%r8, %rcx
	addq	%rcx, %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movsbl	(%rax,%rcx), %eax
	movq	24(%rsp), %rcx
	movslq	16(%rsp), %rdx
	imulq	%r8, %rdx
	addq	%rdx, %rcx
	movslq	16(%rsp), %rdx
	movsbl	(%rcx,%rdx), %ecx
	cmpl	%ecx, %eax
	je	.LBB6_13
# %bb.12:
	jmp	.LBB6_15
.LBB6_13:                               #   in Loop: Header=BB6_10 Depth=1
	jmp	.LBB6_14
.LBB6_14:                               #   in Loop: Header=BB6_10 Depth=1
	movl	16(%rsp), %eax
	addl	$-1, %eax
	movl	%eax, 16(%rsp)
	jmp	.LBB6_10
.LBB6_15:
	cmpl	$0, 16(%rsp)
	jne	.LBB6_18
# %bb.16:
	movq	(%rsp), %rdx                    # 8-byte Reload
	movq	24(%rsp), %rax
	movslq	16(%rsp), %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movslq	16(%rsp), %rcx
	movsbl	(%rax,%rcx), %eax
	cmpl	$32, %eax
	je	.LBB6_18
# %bb.17:
	movq	(%rsp), %rdx                    # 8-byte Reload
	movq	24(%rsp), %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movl	16(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movsbl	(%rax,%rcx), %eax
	movl	%eax, 36(%rsp)
	jmp	.LBB6_45
.LBB6_18:
	movl	$0, 8(%rsp)
.LBB6_19:                               # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_21 Depth 2
	movl	8(%rsp), %eax
	cmpl	20(%rsp), %eax
	jge	.LBB6_31
# %bb.20:                               #   in Loop: Header=BB6_19 Depth=1
	movl	$1, 12(%rsp)
.LBB6_21:                               #   Parent Loop BB6_19 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	12(%rsp), %eax
	cmpl	20(%rsp), %eax
	jge	.LBB6_26
# %bb.22:                               #   in Loop: Header=BB6_21 Depth=2
	movq	(%rsp), %r8                     # 8-byte Reload
	movq	24(%rsp), %rax
	movslq	8(%rsp), %rcx
	imulq	%r8, %rcx
	addq	%rcx, %rax
	movl	12(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movsbl	(%rax,%rcx), %eax
	movq	24(%rsp), %rcx
	movslq	8(%rsp), %rdx
	imulq	%r8, %rdx
	addq	%rdx, %rcx
	movslq	12(%rsp), %rdx
	movsbl	(%rcx,%rdx), %ecx
	cmpl	%ecx, %eax
	je	.LBB6_24
# %bb.23:                               #   in Loop: Header=BB6_19 Depth=1
	jmp	.LBB6_26
.LBB6_24:                               #   in Loop: Header=BB6_21 Depth=2
	jmp	.LBB6_25
.LBB6_25:                               #   in Loop: Header=BB6_21 Depth=2
	movl	12(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 12(%rsp)
	jmp	.LBB6_21
.LBB6_26:                               #   in Loop: Header=BB6_19 Depth=1
	movl	12(%rsp), %eax
	cmpl	20(%rsp), %eax
	jne	.LBB6_29
# %bb.27:                               #   in Loop: Header=BB6_19 Depth=1
	movq	(%rsp), %rdx                    # 8-byte Reload
	movq	24(%rsp), %rax
	movslq	8(%rsp), %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movl	12(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movsbl	(%rax,%rcx), %eax
	cmpl	$32, %eax
	je	.LBB6_29
# %bb.28:
	movq	(%rsp), %rdx                    # 8-byte Reload
	movq	24(%rsp), %rax
	movslq	8(%rsp), %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movl	12(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movsbl	(%rax,%rcx), %eax
	movl	%eax, 36(%rsp)
	jmp	.LBB6_45
.LBB6_29:                               #   in Loop: Header=BB6_19 Depth=1
	jmp	.LBB6_30
.LBB6_30:                               #   in Loop: Header=BB6_19 Depth=1
	movl	8(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 8(%rsp)
	jmp	.LBB6_19
.LBB6_31:
	movl	$0, 12(%rsp)
.LBB6_32:                               # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_34 Depth 2
	movl	12(%rsp), %eax
	cmpl	20(%rsp), %eax
	jge	.LBB6_44
# %bb.33:                               #   in Loop: Header=BB6_32 Depth=1
	movl	$1, 8(%rsp)
.LBB6_34:                               #   Parent Loop BB6_32 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	8(%rsp), %eax
	cmpl	20(%rsp), %eax
	jge	.LBB6_39
# %bb.35:                               #   in Loop: Header=BB6_34 Depth=2
	movq	(%rsp), %r8                     # 8-byte Reload
	movq	24(%rsp), %rax
	movl	8(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	imulq	%r8, %rcx
	addq	%rcx, %rax
	movslq	12(%rsp), %rcx
	movsbl	(%rax,%rcx), %eax
	movq	24(%rsp), %rcx
	movslq	8(%rsp), %rdx
	imulq	%r8, %rdx
	addq	%rdx, %rcx
	movslq	12(%rsp), %rdx
	movsbl	(%rcx,%rdx), %ecx
	cmpl	%ecx, %eax
	je	.LBB6_37
# %bb.36:                               #   in Loop: Header=BB6_32 Depth=1
	jmp	.LBB6_39
.LBB6_37:                               #   in Loop: Header=BB6_34 Depth=2
	jmp	.LBB6_38
.LBB6_38:                               #   in Loop: Header=BB6_34 Depth=2
	movl	8(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 8(%rsp)
	jmp	.LBB6_34
.LBB6_39:                               #   in Loop: Header=BB6_32 Depth=1
	movl	8(%rsp), %eax
	cmpl	20(%rsp), %eax
	jne	.LBB6_42
# %bb.40:                               #   in Loop: Header=BB6_32 Depth=1
	movq	(%rsp), %rdx                    # 8-byte Reload
	movq	24(%rsp), %rax
	movl	8(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movslq	12(%rsp), %rcx
	movsbl	(%rax,%rcx), %eax
	cmpl	$32, %eax
	je	.LBB6_42
# %bb.41:
	movq	(%rsp), %rdx                    # 8-byte Reload
	movq	24(%rsp), %rax
	movl	8(%rsp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movslq	12(%rsp), %rcx
	movsbl	(%rax,%rcx), %eax
	movl	%eax, 36(%rsp)
	jmp	.LBB6_45
.LBB6_42:                               #   in Loop: Header=BB6_32 Depth=1
	jmp	.LBB6_43
.LBB6_43:                               #   in Loop: Header=BB6_32 Depth=1
	movl	12(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 12(%rsp)
	jmp	.LBB6_32
.LBB6_44:
	movl	$32, 36(%rsp)
.LBB6_45:
	movl	36(%rsp), %eax
	addq	$40, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	drow_field;
	.scl	2;
	.type	32;
	.endef
	.globl	drow_field                      # -- Begin function drow_field
	.p2align	4, 0x90
drow_field:                             # @drow_field
.seh_proc drow_field
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movq	%rdx, 64(%rsp)
	movl	%ecx, 60(%rsp)
	movl	60(%rsp), %eax
                                        # kill: def $rax killed $eax
	movq	%rax, 40(%rsp)                  # 8-byte Spill
	movl	$0, 48(%rsp)
	movl	$0, 56(%rsp)
.LBB7_1:                                # =>This Loop Header: Depth=1
                                        #     Child Loop BB7_3 Depth 2
	movl	48(%rsp), %eax
	cmpl	60(%rsp), %eax
	jge	.LBB7_11
# %bb.2:                                #   in Loop: Header=BB7_1 Depth=1
	movl	$0, 52(%rsp)
.LBB7_3:                                #   Parent Loop BB7_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	52(%rsp), %eax
	cmpl	60(%rsp), %eax
	jge	.LBB7_9
# %bb.4:                                #   in Loop: Header=BB7_3 Depth=2
	movq	40(%rsp), %rdx                  # 8-byte Reload
	movq	64(%rsp), %rax
	movslq	48(%rsp), %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movslq	52(%rsp), %rcx
	movsbl	(%rax,%rcx), %eax
	cmpl	$32, %eax
	jne	.LBB7_6
# %bb.5:                                #   in Loop: Header=BB7_3 Depth=2
	movl	56(%rsp), %eax
	addl	$48, %eax
	movl	%eax, 36(%rsp)                  # 4-byte Spill
	jmp	.LBB7_7
.LBB7_6:                                #   in Loop: Header=BB7_3 Depth=2
	movq	40(%rsp), %rdx                  # 8-byte Reload
	movq	64(%rsp), %rax
	movslq	48(%rsp), %rcx
	imulq	%rdx, %rcx
	addq	%rcx, %rax
	movslq	52(%rsp), %rcx
	movsbl	(%rax,%rcx), %eax
	movl	%eax, 36(%rsp)                  # 4-byte Spill
.LBB7_7:                                #   in Loop: Header=BB7_3 Depth=2
	movl	36(%rsp), %edx                  # 4-byte Reload
	movl	52(%rsp), %r8d
	movl	60(%rsp), %r9d
	subl	$1, %r9d
	leaq	"??_C@_03IPAEIDKI@?$HM?$CFc?$AA@"(%rip), %rcx
	leaq	"??_C@_05LFGLBCMB@?$HM?$CFc?$HM?6?$AA@"(%rip), %rax
	cmpl	%r9d, %r8d
	cmoveq	%rax, %rcx
	callq	printf
# %bb.8:                                #   in Loop: Header=BB7_3 Depth=2
	movl	52(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 52(%rsp)
	movl	56(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 56(%rsp)
	jmp	.LBB7_3
.LBB7_9:                                #   in Loop: Header=BB7_1 Depth=1
	jmp	.LBB7_10
.LBB7_10:                               #   in Loop: Header=BB7_1 Depth=1
	movl	48(%rsp), %eax
	addl	$1, %eax
	movl	%eax, 48(%rsp)
	jmp	.LBB7_1
.LBB7_11:
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	printf;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,printf
	.globl	printf                          # -- Begin function printf
	.p2align	4, 0x90
printf:                                 # @printf
.seh_proc printf
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movq	%r9, 104(%rsp)
	movq	%r8, 96(%rsp)
	movq	%rdx, 88(%rsp)
	movq	%rcx, 64(%rsp)
	leaq	88(%rsp), %rax
	movq	%rax, 48(%rsp)
	movq	48(%rsp), %rax
	movq	%rax, 40(%rsp)                  # 8-byte Spill
	movq	64(%rsp), %rax
	movq	%rax, 32(%rsp)                  # 8-byte Spill
	movl	$1, %ecx
	callq	__acrt_iob_func
	movq	32(%rsp), %rdx                  # 8-byte Reload
	movq	40(%rsp), %r9                   # 8-byte Reload
	movq	%rax, %rcx
	xorl	%eax, %eax
	movl	%eax, %r8d
	callq	_vfprintf_l
	movl	%eax, 60(%rsp)
	movl	60(%rsp), %eax
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	get_num;
	.scl	2;
	.type	32;
	.endef
	.text
	.globl	get_num                         # -- Begin function get_num
	.p2align	4, 0x90
get_num:                                # @get_num
.seh_proc get_num
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movq	%rcx, 64(%rsp)
	movl	$1, 56(%rsp)
.LBB9_1:                                # =>This Loop Header: Depth=1
                                        #     Child Loop BB9_4 Depth 2
	cmpl	$0, 56(%rsp)
	jne	.LBB9_3
# %bb.2:                                #   in Loop: Header=BB9_1 Depth=1
	leaq	"??_C@_0BN@OCBJJKFO@incorrect?5input?0?5try?5again?3?5?$AA@"(%rip), %rcx
	callq	printf
.LBB9_3:                                #   in Loop: Header=BB9_1 Depth=1
	movl	$0, 56(%rsp)
	movq	64(%rsp), %rax
	movl	$0, (%rax)
	movl	$1, 48(%rsp)
	movl	$1, 52(%rsp)
.LBB9_4:                                #   Parent Loop BB9_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	callq	getchar
	movl	%eax, 60(%rsp)
	cmpl	$10, %eax
	je	.LBB9_10
# %bb.5:                                #   in Loop: Header=BB9_4 Depth=2
	movl	$0, 48(%rsp)
	cmpl	$48, 60(%rsp)
	jl	.LBB9_8
# %bb.6:                                #   in Loop: Header=BB9_4 Depth=2
	cmpl	$57, 60(%rsp)
	jg	.LBB9_8
# %bb.7:                                #   in Loop: Header=BB9_4 Depth=2
	cmpl	$0, 52(%rsp)
	jne	.LBB9_9
.LBB9_8:                                #   in Loop: Header=BB9_4 Depth=2
	movl	$0, 52(%rsp)
	jmp	.LBB9_4
.LBB9_9:                                #   in Loop: Header=BB9_4 Depth=2
	movq	64(%rsp), %rax
	imull	$10, (%rax), %ecx
	addl	60(%rsp), %ecx
	subl	$48, %ecx
	movq	64(%rsp), %rax
	movl	%ecx, (%rax)
	jmp	.LBB9_4
.LBB9_10:                               #   in Loop: Header=BB9_1 Depth=1
	jmp	.LBB9_11
.LBB9_11:                               #   in Loop: Header=BB9_1 Depth=1
	xorl	%eax, %eax
                                        # kill: def $al killed $al killed $eax
	cmpl	$0, 52(%rsp)
	movb	%al, 47(%rsp)                   # 1-byte Spill
	je	.LBB9_13
# %bb.12:                               #   in Loop: Header=BB9_1 Depth=1
	cmpl	$0, 48(%rsp)
	setne	%al
	xorb	$-1, %al
	movb	%al, 47(%rsp)                   # 1-byte Spill
.LBB9_13:                               #   in Loop: Header=BB9_1 Depth=1
	movb	47(%rsp), %al                   # 1-byte Reload
	xorb	$-1, %al
	testb	$1, %al
	jne	.LBB9_1
# %bb.14:
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	_vsprintf_l;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,_vsprintf_l
	.globl	_vsprintf_l                     # -- Begin function _vsprintf_l
	.p2align	4, 0x90
_vsprintf_l:                            # @_vsprintf_l
.seh_proc _vsprintf_l
# %bb.0:
	subq	$72, %rsp
	.seh_stackalloc 72
	.seh_endprologue
	movq	%r9, 64(%rsp)
	movq	%r8, 56(%rsp)
	movq	%rdx, 48(%rsp)
	movq	%rcx, 40(%rsp)
	movq	64(%rsp), %rax
	movq	56(%rsp), %r9
	movq	48(%rsp), %r8
	movq	40(%rsp), %rcx
	movq	$-1, %rdx
	movq	%rax, 32(%rsp)
	callq	_vsnprintf_l
	nop
	addq	$72, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	_vsnprintf_l;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,_vsnprintf_l
	.globl	_vsnprintf_l                    # -- Begin function _vsnprintf_l
	.p2align	4, 0x90
_vsnprintf_l:                           # @_vsnprintf_l
.seh_proc _vsnprintf_l
# %bb.0:
	subq	$136, %rsp
	.seh_stackalloc 136
	.seh_endprologue
	movq	176(%rsp), %rax
	movq	%r9, 128(%rsp)
	movq	%r8, 120(%rsp)
	movq	%rdx, 112(%rsp)
	movq	%rcx, 104(%rsp)
	movq	176(%rsp), %rax
	movq	%rax, 88(%rsp)                  # 8-byte Spill
	movq	128(%rsp), %rax
	movq	%rax, 80(%rsp)                  # 8-byte Spill
	movq	120(%rsp), %rax
	movq	%rax, 72(%rsp)                  # 8-byte Spill
	movq	112(%rsp), %rax
	movq	%rax, 64(%rsp)                  # 8-byte Spill
	movq	104(%rsp), %rax
	movq	%rax, 56(%rsp)                  # 8-byte Spill
	callq	__local_stdio_printf_options
	movq	56(%rsp), %rdx                  # 8-byte Reload
	movq	64(%rsp), %r8                   # 8-byte Reload
	movq	72(%rsp), %r9                   # 8-byte Reload
	movq	80(%rsp), %r10                  # 8-byte Reload
	movq	%rax, %rcx
	movq	88(%rsp), %rax                  # 8-byte Reload
	movq	(%rcx), %rcx
	orq	$1, %rcx
	movq	%r10, 32(%rsp)
	movq	%rax, 40(%rsp)
	callq	__stdio_common_vsprintf
	movl	%eax, 100(%rsp)
	cmpl	$0, 100(%rsp)
	jge	.LBB11_2
# %bb.1:
	movl	$4294967295, %eax               # imm = 0xFFFFFFFF
	movl	%eax, 52(%rsp)                  # 4-byte Spill
	jmp	.LBB11_3
.LBB11_2:
	movl	100(%rsp), %eax
	movl	%eax, 52(%rsp)                  # 4-byte Spill
.LBB11_3:
	movl	52(%rsp), %eax                  # 4-byte Reload
	addq	$136, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.def	__local_stdio_printf_options;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,__local_stdio_printf_options
	.globl	__local_stdio_printf_options    # -- Begin function __local_stdio_printf_options
	.p2align	4, 0x90
__local_stdio_printf_options:           # @__local_stdio_printf_options
# %bb.0:
	leaq	__local_stdio_printf_options._OptionsStorage(%rip), %rax
	retq
                                        # -- End function
	.def	_vfprintf_l;
	.scl	2;
	.type	32;
	.endef
	.section	.text,"xr",discard,_vfprintf_l
	.globl	_vfprintf_l                     # -- Begin function _vfprintf_l
	.p2align	4, 0x90
_vfprintf_l:                            # @_vfprintf_l
.seh_proc _vfprintf_l
# %bb.0:
	subq	$104, %rsp
	.seh_stackalloc 104
	.seh_endprologue
	movq	%r9, 96(%rsp)
	movq	%r8, 88(%rsp)
	movq	%rdx, 80(%rsp)
	movq	%rcx, 72(%rsp)
	movq	96(%rsp), %rax
	movq	%rax, 64(%rsp)                  # 8-byte Spill
	movq	88(%rsp), %rax
	movq	%rax, 56(%rsp)                  # 8-byte Spill
	movq	80(%rsp), %rax
	movq	%rax, 48(%rsp)                  # 8-byte Spill
	movq	72(%rsp), %rax
	movq	%rax, 40(%rsp)                  # 8-byte Spill
	callq	__local_stdio_printf_options
	movq	40(%rsp), %rdx                  # 8-byte Reload
	movq	48(%rsp), %r8                   # 8-byte Reload
	movq	56(%rsp), %r9                   # 8-byte Reload
	movq	%rax, %rcx
	movq	64(%rsp), %rax                  # 8-byte Reload
	movq	(%rcx), %rcx
	movq	%rax, 32(%rsp)
	callq	__stdio_common_vfprintf
	nop
	addq	$104, %rsp
	retq
	.seh_endproc
                                        # -- End function
	.lcomm	field,9                         # @field
	.section	.rdata,"dr",discard,"??_C@_0CK@KBKEEGHN@?$CFc?5step?0?5enter?5pos?$CInumber?5from?50@"
	.globl	"??_C@_0CK@KBKEEGHN@?$CFc?5step?0?5enter?5pos?$CInumber?5from?50@" # @"??_C@_0CK@KBKEEGHN@?$CFc?5step?0?5enter?5pos?$CInumber?5from?50@"
"??_C@_0CK@KBKEEGHN@?$CFc?5step?0?5enter?5pos?$CInumber?5from?50@":
	.asciz	"%c step, enter pos(number from 0 to %d): "

	.section	.rdata,"dr",discard,"??_C@_0P@NNHNHGBC@out?5of?5range?0?5?$AA@"
	.globl	"??_C@_0P@NNHNHGBC@out?5of?5range?0?5?$AA@" # @"??_C@_0P@NNHNHGBC@out?5of?5range?0?5?$AA@"
"??_C@_0P@NNHNHGBC@out?5of?5range?0?5?$AA@":
	.asciz	"out of range, "

	.section	.rdata,"dr",discard,"??_C@_0BD@NJLHBFAJ@cell?5is?5occupied?0?5?$AA@"
	.globl	"??_C@_0BD@NJLHBFAJ@cell?5is?5occupied?0?5?$AA@" # @"??_C@_0BD@NJLHBFAJ@cell?5is?5occupied?0?5?$AA@"
"??_C@_0BD@NJLHBFAJ@cell?5is?5occupied?0?5?$AA@":
	.asciz	"cell is occupied, "

	.section	.rdata,"dr",discard,"??_C@_0M@OPNOJLIB@try?5again?3?5?$AA@"
	.globl	"??_C@_0M@OPNOJLIB@try?5again?3?5?$AA@" # @"??_C@_0M@OPNOJLIB@try?5again?3?5?$AA@"
"??_C@_0M@OPNOJLIB@try?5again?3?5?$AA@":
	.asciz	"try again: "

	.section	.rdata,"dr",discard,"??_C@_08NKNFNOFB@?$CFc?5win?$CB?6?$AA@"
	.globl	"??_C@_08NKNFNOFB@?$CFc?5win?$CB?6?$AA@" # @"??_C@_08NKNFNOFB@?$CFc?5win?$CB?6?$AA@"
"??_C@_08NKNFNOFB@?$CFc?5win?$CB?6?$AA@":
	.asciz	"%c win!\n"

	.section	.rdata,"dr",discard,"??_C@_08CCICKHPI@nobody?8s?$AA@"
	.globl	"??_C@_08CCICKHPI@nobody?8s?$AA@" # @"??_C@_08CCICKHPI@nobody?8s?$AA@"
"??_C@_08CCICKHPI@nobody?8s?$AA@":
	.asciz	"nobody's"

	.section	.rdata,"dr",discard,"??_C@_05LFGLBCMB@?$HM?$CFc?$HM?6?$AA@"
	.globl	"??_C@_05LFGLBCMB@?$HM?$CFc?$HM?6?$AA@" # @"??_C@_05LFGLBCMB@?$HM?$CFc?$HM?6?$AA@"
"??_C@_05LFGLBCMB@?$HM?$CFc?$HM?6?$AA@":
	.asciz	"|%c|\n"

	.section	.rdata,"dr",discard,"??_C@_03IPAEIDKI@?$HM?$CFc?$AA@"
	.globl	"??_C@_03IPAEIDKI@?$HM?$CFc?$AA@" # @"??_C@_03IPAEIDKI@?$HM?$CFc?$AA@"
"??_C@_03IPAEIDKI@?$HM?$CFc?$AA@":
	.asciz	"|%c"

	.section	.rdata,"dr",discard,"??_C@_0BN@OCBJJKFO@incorrect?5input?0?5try?5again?3?5?$AA@"
	.globl	"??_C@_0BN@OCBJJKFO@incorrect?5input?0?5try?5again?3?5?$AA@" # @"??_C@_0BN@OCBJJKFO@incorrect?5input?0?5try?5again?3?5?$AA@"
"??_C@_0BN@OCBJJKFO@incorrect?5input?0?5try?5again?3?5?$AA@":
	.asciz	"incorrect input, try again: "

	.lcomm	__local_stdio_printf_options._OptionsStorage,8,8 # @__local_stdio_printf_options._OptionsStorage
	.addrsig
	.addrsig_sym _vsnprintf
	.addrsig_sym init_field
	.addrsig_sym victory_check
	.addrsig_sym drow_field
	.addrsig_sym printf
	.addrsig_sym get_num
	.addrsig_sym getchar
	.addrsig_sym _vsprintf_l
	.addrsig_sym _vsnprintf_l
	.addrsig_sym __stdio_common_vsprintf
	.addrsig_sym __local_stdio_printf_options
	.addrsig_sym _vfprintf_l
	.addrsig_sym __acrt_iob_func
	.addrsig_sym __stdio_common_vfprintf
	.addrsig_sym field
	.addrsig_sym __local_stdio_printf_options._OptionsStorage
