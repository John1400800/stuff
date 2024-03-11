if &t_Co >= 256 
    set termguicolors
    colorscheme mycolorscheme
else
    set background=dark
endif

syntax on

" insert cursor vert line
let &t_SI = "\<Esc>[6 q"
let &t_EI = "\<Esc>[2 q"

set noswapfile
set clipboard=unnamedplus

set laststatus=2
set showcmd
set wildmenu

set cursorline
set cursorlineopt=number

set relativenumber
set number
set numberwidth=3

set shiftwidth=4
set expandtab
set smarttab
set smartindent

set ignorecase
set smartcase
set incsearch
nmap <F4> :set hlsearch!<cr>

set scrolloff=5
