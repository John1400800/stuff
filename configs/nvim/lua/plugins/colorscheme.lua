return {
  
    'rose-pine/neovim',
    name = 'rose-pine',
    lazy = true,
    priority = 1000,
    opts = {
      variant = "main",
      disable_italics = true,
      disable_background = true,
      highlight_groups = {
        CursorLine = { bg = 'foam', blend = 10 },
        Search = { bg = 'gold', inherit = false },
      },
    },
  
}
