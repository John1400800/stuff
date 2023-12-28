return {

  {
    "m4xshen/autoclose.nvim",
    opts = {
      options = {
        pair_spaces = true,
      },
    },
  },

  {
    'hrsh7th/nvim-cmp',
    dependencies = {
      'neovim/nvim-lspconfig',
      'hrsh7th/cmp-nvim-lsp',
      'saadparwaiz1/cmp_luasnip',
      'L3MON4D3/LuaSnip',
      -- 'rafamadriz/friendly-snippets',
    },
    config = function()
      local keymap_set = vim.keymap.set
      local lsp_buf = vim.lsp.buf
      keymap_set('n', '<space>e', vim.diagnostic.open_float)
      keymap_set('n', '[d', vim.diagnostic.goto_prev)
      keymap_set('n', ']d', vim.diagnostic.goto_next)
      keymap_set('n', '<space>q', vim.diagnostic.setloclist)
      
      -- Use LspAttach autocommand to only map the following keys
      -- after the language server attaches to the current buffer
      vim.api.nvim_create_autocmd('LspAttach', {
        group = vim.api.nvim_create_augroup('UserLspConfig', {}),
        callback = function(ev)
          -- Buffer local mappings.
          -- See `:help vim.lsp.*` for documentation on any of the below functions
          local opts = { buffer = ev.buf }
          keymap_set('n', 'gD', lsp_buf.declaration, opts)
          keymap_set('n', 'gd', lsp_buf.definition, opts)
          keymap_set('n', 'K', lsp_buf.hover, opts)
          keymap_set('n', 'gi', lsp_buf.implementation, opts)
          keymap_set('n', '<C-k>', lsp_buf.signature_help, opts)
          keymap_set('n', '<space>wa', lsp_buf.add_workspace_folder, opts)
          keymap_set('n', '<space>wr', lsp_buf.remove_workspace_folder, opts)
          keymap_set('n', '<space>wl', function()
            print(vim.inspect(lsp_buf.list_workspace_folders()))
          end, opts)
          keymap_set('n', '<space>D', lsp_buf.type_definition, opts)
          keymap_set('n', '<space>rn', lsp_buf.rename, opts)
          keymap_set({ 'n', 'v' }, '<space>ca', lsp_buf.code_action, opts)
          keymap_set('n', 'gr', lsp_buf.references, opts)
          keymap_set('n', '<space>f', function()
            lsp_buf.format { async = true, }
          end, opts)
        end,
      })
      -- Snip
      -- require("luasnip.loaders.from_vscode").lazy_load()

      vim.diagnostic.config({
        virtual_text = {
          prefix = '●', -- Could be '■', '▎', 'x'
        }
      })

      -- Add additional capabilities supported by nvim-cmp
      local capabilities = require("cmp_nvim_lsp").default_capabilities()
      
      local lspconfig = require('lspconfig')
      
      -- Enable some language servers with the additional completion capabilities offered by nvim-cmp
      local servers = { 'clangd', 'pyright' }
      for _, lsp in ipairs(servers) do
        lspconfig[lsp].setup {
          -- on_attach = my_custom_on_attach,
          capabilities = capabilities,
        }
      end
      
      -- luasnip setup
      local luasnip = require 'luasnip'
      
      -- nvim-cmp setup
      local cmp = require 'cmp'
      cmp.setup {
        snippet = {
          expand = function(args)
            luasnip.lsp_expand(args.body)
          end,
        },
        mapping = cmp.mapping.preset.insert({
          ['<C-u>'] = cmp.mapping.scroll_docs(-4), -- Up
          ['<C-d>'] = cmp.mapping.scroll_docs(4), -- Down
          -- C-b (back) C-f (forward) for snippet placeholder navigation.
          ['<C-x>'] = cmp.mapping.complete(), --'<C-Space>'
          ['<CR>'] = cmp.mapping.confirm {
            behavior = cmp.ConfirmBehavior.Replace,
            select = true,
          },
          ['<Tab>'] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_next_item()
            elseif luasnip.expand_or_jumpable() then
              luasnip.expand_or_jump()
            else
              fallback()
            end
          end, { 'i', 's' }),
          ['<S-Tab>'] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_prev_item()
            elseif luasnip.jumpable(-1) then
              luasnip.jump(-1)
            else
              fallback()
            end
          end, { 'i', 's' }),
        }),
        sources = {
          { name = 'nvim_lsp' },
          { name = 'luasnip' },
        },
      }
    end,
  },

}
