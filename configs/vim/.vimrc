syntax on

let &t_SI = "\<Esc>[6 q"
let &t_EI = "\<Esc>[2 q"

set showcmd
set wildmenu
set laststatus=2
set clipboard=unnamed,unnamedplus

set relativenumber
set number
set numberwidth=3

set shiftwidth=4
set expandtab
set smartindent
set smarttab

set ignorecase
set smartcase
set incsearch

set scrolloff=5
set noswapfile

" autoclose bracket
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O
