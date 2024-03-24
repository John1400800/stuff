set nocompatible

if &t_Co>=2
    syntax on
    if &t_Co>=256
        set termguicolors
        colorscheme mycolorscheme
        if !has("gui_running")
            let &t_SI="\<Esc>[6 q"
            let &t_EI="\<Esc>[2 q"
        endif
    endif
endif

filetype plugin indent on

set directory   =$HOME/.vim/swp//
set nowritebackup

set autoread

set lazyredraw

set clipboard	=unnamedplus

set expandtab
set shiftwidth	=4
set smarttab
set smartindent

set incsearch
set hlsearch
set ignorecase
set smartcase

set number
set relativenumber
set numberwidth	=3

set cursorline
set cursorlineopt=number

set laststatus	=2
set showcmd
set wildmenu
set wildoptions	=fuzzy,pum,tagfile

set scrolloff	=5
set sidescrolloff=5

let g:netrw_liststyle=3
let g:netrw_winsize  =22

nnoremap <F4>	:nohlsearch<cr>
