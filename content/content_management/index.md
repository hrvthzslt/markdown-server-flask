---
title: Content management
---

# Content management

This is a simple content management system that uses Flask and Markdown to serve content from a directory. The content is written in Markdown and converted to HTML on the fly.

## Routing

Routes are defined by the file structure in the `content` directory. The content of the page is found in the current directory's `index.md` file.

[Route example](content_management/route_example)

## Meta data

Optional meta data can be added in the markdown file in frontmatter format. The only required field is `title`, this is used as the page title.

```markdown
---
title: Page title
---
```

[Back](/)
