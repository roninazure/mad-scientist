name:  Auto-Update README

permissions:
  contents: write

on:
  schedule:
    - cron: "0 4 * * *"
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest

    steps:
      - name:  Checkout repo
        uses: actions/checkout@v4

      - name:  Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.x"

      - name:  Install Python dependencies
        run: pip install -r requirements.txt

      - name:  Run updater script
        run: python .github/scripts/update_readme.py

      - name:  Commit changes
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email '41898282+github-actions[bot]@users.noreply.github.com'
          git pull --rebase origin main
          git add README.md
          git commit -m "Auto-update README" || echo "No changes"
          git push origin main
