# gitnote ✍️

**`gitnote` is a CLI tool that uses AI to automatically generate meaningful Git commit messages based on staged changes.**

&nbsp;
&nbsp;

# Overview 🔎
`gitnote` is an intelligent CLI tool designed for automatically generating commit messages with the help of artificial intelligence. This tool analyzes the staged changes in your Git repository to assist you in writing more relevant and optimized commit messages, improving your Git workflow.



&nbsp;

# Features ✨

- **Smart Commit Message Suggestion:** Powered by Hugging Face Hub, this tool suggest commit messages tailored to your staged changes.
- **Clear and Enhanced Display:** Uses the `rich` package to beautifully render staged changes in the CLI.
- **User-Friendly CLI Interface:** Built with `typer`, `gitnote` offers an intuitive and easy-to-use command-line interface.

&nbsp;

# Installation 📥

To install `gitnote`, use pip:

```bash
pip install gitnote
```

&nbsp;

# Initial Setup ⚡

Before using `gitnote`, take your token from [Hugging Face API token](https://huggingface.co/settings/tokens) **(Recommended first!)** and run the following command to set the token :


```bash
gitnote set-token
```

You can also set the token like this :

```bash
gitnote set-token "<token>"
```
> **_Note:_** Don't forget put token inside double quotes on second way!

&nbsp;

# Usage 💡

### Available Commands

- `gitnote diff`
   Displays the staged changes in a visually enhanced format. If no changes are staged, the following message is displayed:

   ```bash
   No changes to display.
   ```

- `gitnote generate`
   Takes the staged changes (if any) and sends them to the Hugging Face Hub to generate an AI-driven commit message. If there are no staged changes, you’ll see:

   ```
   ⚠️ No staged changes found! Please make sure you've staged your changes using 'git add' and try again.
   ```

### Help Command

For a full list of commands and usage information, use:

```bash
gitnote --help
```

&nbsp;

# Dependencies 🛠️

This project is built with the following key packages:

- `typer`: For creating a command-line interface (CLI)
- `huggingface-hub`: For connecting to Hugging Face AI models to generate intelligent commit messages
- `rich`: For beautifully rendering the staged changes in the CLI

> The complete list of dependencies can be found in the `requirements.txt` file.

&nbsp;

# gitnote preview :
[gitntoe_preview](assets/preview/gitnote_preview.mp4)

# License 🧾

This project is licensed under the [MIT License](./LICENSE).
