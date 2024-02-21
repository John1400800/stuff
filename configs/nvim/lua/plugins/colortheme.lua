return {

  {
    "blazkowolf/gruber-darker.nvim", 
  },
  
  {
    "ellisonleao/gruvbox.nvim",
    name = "gruvbox",
    lazy = true,
    priority = 1000,
  },

  {
    'rose-pine/neovim',
    name = 'rose-pine',
    lazy = true,
    priority = 1000,
    opts = {
      -- variant = "moon",
      -- disable_italics = true,
      disable_background = true,
      highlight_groups = {
        CursorLine = { bg = 'foam', blend = 10 },
        Search = { bg = 'gold', inherit = false, },
      },
    },
  },

}
