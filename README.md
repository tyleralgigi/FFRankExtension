# FFRankExtension

**FFRankExtension** is a Chrome extension designed to enhance your fantasy football drafting experience on the Sleeper platform. It introduces a custom "Rank" column directly into the Sleeper draft board, allowing you to manage and view player rankings without relying on external spreadsheets.

<em>The data in this project currently is from 2023. It will be updated for the 2025 season</em>

## Features

- **Custom Rank Integration:** Seamlessly integrates a new Rank column into the Sleeper draft interface, allowing users to identify undervalued and overvalued players by comparing the site's current rankings with custom rankings.
- **User-Friendly Interface:** Designed to blend naturally with the existing Sleeper UI for an intuitive drafting experience.

## Preview
![Preview](https://i.imgur.com/OtOCHJK.png)
<em>Currently, the only working options are Sleeper and PPR</em>
## Installation

### Clone or Download the Repository:

```bash
git clone https://github.com/tyleralgigi/FFRankExtension.git
```

Alternatively, download the ZIP file from the repository and extract its contents.

### Load the Extension in Chrome:

1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable "Developer mode" using the toggle switch in the top right corner.
3. Click on the "Load unpacked" button.
4. Select the directory containing the extracted or cloned FFRankExtension files.

### Confirm Installation:

- Once loaded, the FFRankExtension should appear in your list of Chrome extensions.
- Ensure the extension is enabled.

## Usage

### Navigate to Sleeper Draft Board:

- Log in to your Sleeper account and access your league's draft board.

### Activate the Extension:

- The extension will automatically inject the "Rank" column into the draft board interface.
- You can interact with this column to view or adjust player rankings as needed.

## Code Overview

- **`manifest.json`** - Defines the extension's metadata, permissions, and scripts to be executed.
- **`content.js`** - Contains the primary logic for injecting and managing the "Rank" column within the Sleeper draft board.
- **`custom.css`** - Styles the injected "Rank" column to ensure it aligns with the existing Sleeper design.
- **`popup.html` & `popup.js`** - Manage the extension's popup interface, allowing users to interact with settings or features outside the draft board.
- **`sleeper ranking.csv`** - A CSV file containing player rankings, which the extension reads to populate the "Rank" column.

## Contributing

We welcome contributions to enhance the FFRankExtension. To contribute:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Description of feature or fix'
   ```

4. Push to the branch:

   ```bash
   git push origin feature-name
   ```

5. Open a Pull Request detailing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.

## Acknowledgments

Special thanks to the Sleeper team for providing a robust platform for fantasy football enthusiasts and to all contributors who have helped improve this extension.
