# fcg
Flashcard generator - A small gift for my son's first birthday

#### System
- Ubuntu Linux

#### How to run
- Create *conda* environment
```
$ conda env create -n <env_name> -f requirements.txt
```

- Activate created environment
```
$ source activate <env_name>
```

- Run spider
```
$ scrapy crawl flags
```

There will be an *output<xx>.odt* file created under *<project_root>/output* folder. When open that file, there should be a warning about the file is corrupt but you can click *yes* to repare it 
(this is due to the file is created by the script). When the file is opened you can save it or export it to PDF from menu bar.

#### Sample Output
![Sample](samples/sample1.png)

#### Full pre-generated PDF file
[Flags flashcards full](samples/flashcards_full.pdf)
