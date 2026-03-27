import { QuartzConfig } from "./quartz/shared"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4.0 Configuration
 **/
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Vault Corporativo BSO Datasul",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "pt-BR",
    baseUrl: "joaoribeiro-Vault.github.io/vault-corporativo",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#ffffff", // Fundo branco limpo
          lightgray: "#f0f0f0", // Bordas suaves
          gray: "#b8b8b8",
          darkgray: "#4e4e4e", // Texto principal
          dark: "#1a1a1a", // Títulos fortes
          secondary: "#00B2A9", // Ciano TOTVS (Cor principal)
          tertiary: "#00857D", // Ciano Escuro (Cor do hover)
          highlight: "rgba(0, 178, 169, 0.10)", // Fundo de destaque suave
          textHighlight: "rgba(0, 178, 169, 0.25)",
        },
        darkMode: {
          light: "#161618", // Fundo escuro elegante (não 100% preto)
          lightgray: "#393639", // Bordas no modo escuro
          gray: "#646464",
          darkgray: "#d4d4d4", // Texto principal claro
          dark: "#ebebec", // Títulos brancos
          secondary: "#00D4C9", // Ciano TOTVS mais brilhante para dar contraste
          tertiary: "#00B2A9", // Ciano padrão no hover
          highlight: "rgba(0, 212, 201, 0.15)",
          textHighlight: "rgba(0, 212, 201, 0.25)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config