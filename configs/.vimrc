if &t_Co>=2
    syntax on
endif
if &t_Co>=256 
    set termguicolors
    colorscheme mycolorscheme
    if !has("gui_running")
        let &t_SI="\<Esc>[6 q"
        let &t_EI="\<Esc>[2 q"
    endif
endif

filetype plugin indent on

set noswapfile
set clipboard   =unnamedplus

set laststatus  =2
set showcmd
set wildmenu
set wildoptions =fuzzy,pum,tagfile

set cursorline
set cursorlineopt=number

set relativenumber
set number
set numberwidth =3

set shiftwidth  =4
set expandtab
set smarttab
set smartindent

set ignorecase
set smartcase
set incsearch

set scrolloff   =5

nnoremap <F4>   :set hlsearch!<cr>
