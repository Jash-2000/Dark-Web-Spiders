# Iron March SQL Database

This archive contains the SQL database dump of a backup of the Iron March forum, as well as scripts for converting the separate tables in the database into CSV files, and the CSV files themselves in the directory `csv/`.
The original link was posted to Iron March's successor forum Fascist Forge in the post https://fascistforge.com/index.php?app=forums&module=forums&controller=topic&id=666, but that link is now dead.

A mirror for an archive containing the database is the following website https://www.bthub.me/hash/1d0554862068bfaba9bd2fc6f75cb69fa420c834 which hosts a magnet link that can be used to download the database by opening the following URL in a torrent client:
magnet:?xt=urn:btih:1d0554862068bfaba9bd2fc6f75cb69fa420c834
and selecting the file "The Archives/Iron March - NOOSE Backups/Iron March - Rope Culture Website Backups/Iron March - Rope Culture Backups/database.sql"

Currently the scripts to convert the SQL dump into CSV files only work on a Linux OS.
To extract CSV files of all tables in the database, run the following scripts in the specified order (from the `scripts/` directory):

```console
bash split_sql_tables.sh
python rename_dumps.py
bash convert_to_sqlite.sh
bash convert_to_csv.sh
```

The script `convert_to_sqlite.sh` requires the script `mysql2sqlite`, which was
downloaded from https://github.com/dumblob/mysql2sqlite
You will likely need to enable the file `mysql2sqlite` to run as an executable, using the following command:

```console
chmod +x mysql2sqlite
```

The prerequisites needed to execute these scripts are:
- Python distribution with default libraries
- sqlite3 distribution

## About IronMarch

Iron March was founded in 2011 and shut down in November 2017, likely due to repeated hacking designed to disrupt the site. The leaked data shows Iron March was created by a 
Russia-based individual going by the alias Alexander “Slavros” Mukhitdinov, referred to as “Slavros.” According to the SPLC’s research, Slavros kept very close control of the 
public posts on the site and also managed another site, Slavros.org, which was registered under the name Alisher Mukhitdinov and posted similar content. After Iron March was 
taken down in November 2017, Slavros appears to have halted online activity and no one has reported contact with him. On a site built to follow Iron March, called Fascist Forge, members speculated that Slavros was arrested by the Russian government.
Iron March was structured as a standard web forum/message board. It allowed any visitor to view and read material, while providing members with the capability to make public 
posts on the several broad threads created by the administrator. Additionally, the site had a private message feature and hosted administrative material, including member 
guidelines and a calendar, which primarily noted the birthdays of historically significant facsist figures. During its six years of activity, Iron March acted as a hub for 
neo-Nazi and white supremacist groups around the world. The website had approximately 1,200 regular users and was affiliated with at least nine different neo-Nazi or white 
supremacist groups. Among them are Atomwaffen Division (or atomic weapons division) in the United States, the United Kingdom-based and now banned National Action, the 
Scandinavian Nordic Resistance Movement, and the Australian Antipodean Resistance.

Using Ironmarch.org, these groups and other Iron March users recruited and refined their violent white supremacist ideology. According to SPLC, Iron March users and associated 
groups did not strictly adhere to any one doctrine. Rather, the website allowed its members to actively discuss global fascist literature and adopt their own interpretations of
fascist doctrine.

SPLC has also reported that groups associated with Iron March were linked to numerous instances of white extremist violence around the world. In July 2017, the Nordic Resistance
Movement was responsible for an attack on a Swedish refugee center as well as several other bombings. In October 2017, an unnamed member of the U.K.-based National Action 
movement was accused of plotting with the group’s leader to assassinate Rosie Cooper, a 67-year-old Labor member of the U.K. Parliament. A year earlier, the British government
made being a member of National Action illegal after one of the group’s members killed Jo Cox, a British member of parliament, with a homemade rifle.

In the United States, Atomwaffen Division’s founder, Brandon Russell, a member of the Florida National Guard, was convicted on Jan. 9, 2018, of charges related to explosive 
materials found on his premises. Prior to Russell’s conviction, he worked closely with Slavros on Iron March to build Atomwaffen and recruit members. Through Iron March, 
Russell and early Atomwaffen leadership discovered the writings of James Mason, a Charles Manson acolyte and an American neo-Nazi. Mason’s collective works, entitled 
“SIEGE,” were written in the 1980s and advocate for white revolution through terrorism conducted by individual cells. Atomwaffen Division fully adopted this ideology and 
received direct support from James Mason. The group’s members have been linked to a range of violent activity, including an attempted bombing and heavy weapons assault on a 
Halifax mall in Canada. More recently, in November 2019, the leader of an Atomwaffen Division cell based in the state of Washington was stopped in Texas with illegal 
assault-style rifles and up to 2,000 rounds of ammunition.
Active Iron March users were also critical decision-makers behind the Unite the Right rally that took place in Charlottesville, Virginia, on Aug. 11-12, 2017. 
The rally led to numerous instances of violence enacted by white supremacist groups against counter protesters, including a vehicular attack that killed Heather Heyer and 
injured 28 others. A civil complaint was filed on Sept. 17, 2019, in U.S. District Court for the Western District of Virginia against 25 individuals and organizations related 
to the Charlottesville rally. At least five of the individuals or organizations listed in that complaint had active accounts on Iron March.
