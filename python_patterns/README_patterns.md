# Markdown Patterns for README & Design Docs

## 1. Headers
```md
# H1 Header (Title)
## H2 Header (Section)
### H3 Header (Subsection)
#### H4 Header (Smaller Subsection)
```

## 2. Text Formatting
```md
*Italic text*  
**Bold text**  
~~Strikethrough~~  
`Inline code`  
```

## 3. Lists
```md
### Unordered List
- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2

### Ordered List
1. First item
2. Second item
   1. Sub-item
   2. Sub-item
```

## 4. Links & Images
```md
[Link to Google](https://www.google.com)

![Image Alt Text](https://via.placeholder.com/150)
```

## 5. Blockquotes
```md
> This is a blockquote.
> Use it to highlight important information.
```

## 6. Code Blocks
```md
### Inline Code
`print("Hello, World!")`

### Multi-line Code Block
```python
print("Hello, World!")
for i in range(5):
    print(i)
```
```

## 7. Tables
```md
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data 1   | Data 2   |
| Row 2    | Data 3   | Data 4   |
```

## 8. Checklists (Task Lists)
```md
- [x] Task 1 (Completed)
- [ ] Task 2 (Not Done)
```

## 9. Horizontal Line (Separator)
```md
---
```

## 10. Emojis (GitHub & Slack supported)
```md
🚀 :rocket:
✅ :white_check_mark:
```

## 11. Footnotes
```md
This is a sentence with a footnote.[^1]

[^1]: This is the footnote text.
```

## 12. Collapsible Sections
```md
<details>
  <summary>Click to expand</summary>
  Hidden content here.
</details>
```

## 13. Mermaid Diagrams (GitHub Supported)
```md
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
```
