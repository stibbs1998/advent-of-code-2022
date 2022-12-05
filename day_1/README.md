Did this one as a Bash Command!

```
echo '1000                                                                                                                                                       
2000
3000

4000

5000
6000

7000
8000
9000

10000' >> input.txt && mkdir elves/ && awk -v RS= '{print > ("elves/elf-" NR ".txt")}' input.txt && for file in $(ls elves/); do; awk '{ sum += $1 } END { print sum }' elves/$file >> output.txt; done && sed '=' output.txt | sed 'N; s/\n/ /' | sort -nk 2 | tail -1
```
