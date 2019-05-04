# FCG
Flashcard generator - A small gift for my son's first birthday and all kids


#### System
- Ubuntu Linux
- Anaconda3 (conda 4.4.10)
- LibreOffice 5.1.6.2 10m0(Build:2)


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

There will be an *output\<xxx\>.odt* file created under *\<project_root\>/output* folder. When open that file, there should be a warning about the file is corrupt but you can click *yes* to repare it 
(this is due to the file is created by the script). When the file is opened you can save it or export it to PDF from menu bar.


#### Sample Output
- Countries' Flags sample

![Countries' Flags sample](samples/countries_flags_sample1.png)

- Car brands sample
![Countries' Flags sample](samples/carbrands_sample1.png)


#### Full pre-generated PDF file
- [Countries' Flags flashcards full](samples/countries_flags_full.pdf)
- [Car brands flashcards full](samples/carbrands_full.pdf)
