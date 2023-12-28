return {
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    opts = {
        ensure_installed = { "c", "lua", "python", "cpp", "rust", },
        highlight = { enable = true, },
    },

    config = function(_, opts)
      require 'nvim-treesitter.install'.compilers = { "clang" }
      require 'nvim-treesitter.configs'.setup(opts)
    end,
  },
}
