# Word_Cloud
http://www.cs.middlebury.edu/~candrews/showcase/infovis_techniques_s16/sparkclouds/sparkcloud.html

Repository for our presentation on SparkClouds.
Aayam Poudel and Jamie Hand

Our process:

1. Got text of State of the Union addresses from 2001 to 2016
and put them into .txt files.

2. Wrote a python script to strip new lines and punctuation,
extract each word (excluding stop words like "the", "a", "I", and "will"),
count how many times it appears, and put them in a list in order of their
frequency.

3. Output these words, counts, and years to a CSV file, and
combined the CSV files into a single file.

4. Wrote an HTML page with a demo, showing a SparkCloud that
takes in the CSV as data.

TODO:

- Each sparkline should have its own domain and range.
