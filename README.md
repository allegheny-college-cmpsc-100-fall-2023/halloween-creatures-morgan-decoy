# Halloween Creatures & Mouse Interaction

In this exercise, you will get practice with Github, VPython textures, and importing local files into your python project. 

> [!NOTE]  
> If you make changes to the repo in the web browser, you need to run `git pull` to get them into the local version. We will learn more about git in the coming weeks, but for now it's better if you make edits to your repo ONLY on your computer or ONLY in the browser. Mixing and matching can cause conflicts. 

## Instructions 

1. Open you CMPSC-100 folder in VSCode.
2. Copy the clone link for this repo by clicking the \<Code\> dropdown just above the list of files, then choose SSH and hit the double-square copy icon. Open the Terminal in VSCode with Terminal>New Terminal then enter `git clone <text you just copied>`. When repo finishes cloning, `cd` into the new directory. 
    <img src = 'copy_thumbnail.png' width = "300px" />
3. Follow along with professor to write a function called `pumpkin` that draws a pumpkin in `models.py`, and deploy it in `main.py`. Save your changes in both files with File>Save, CTRL+S (PC), or CMND+S (Mac). 
4. Using what you learned during Step 3, write a function called `alien` in `models.py` with `pos` as its first parameter. Find or make an alien face jpeg or png to use as the texture, download it into this repo, and wrap it around an [`ellipsoid` shape](https://www.glowscript.org/docs/VPythonDocs/ellipsoid.html). Save your changes.
5. In `main.py`, replace the `black_cat` function with your `alien` function.  Save your changes.
6. Run `gatorgrade` in the VSCode Terminal to see how you're doing.
7. When you're ready, push your changes to github with the following Terminal commands:
```
git add .
git commit -m "update halloween creatures"
git push

```

