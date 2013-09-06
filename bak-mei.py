import sys, os, shutil, subprocess

SEARCH_REPLACE_SCRIPT = os.path.expanduser(
    "~/src/Search-Replace-DB/searchreplacedb2cli.php")

SEARCH_REPLACE_CMD = ("{SEARCH_REPLACE_SCRIPT} -h {host} -u {user} -d {db} -p"
                      " {password} -s {search} -r {replace} ")

def search_replace_cmd(**kwargs):
    return ["php", SEARCH_REPLACE_SCRIPT, "-h", kwargs["host"], "-u",
            kwargs["user"], "-d", kwargs["db"], "-p", kwargs["pwd"], "-s",
            kwargs["search"], "-r", kwargs["replace"]]

if __name__ == "__main__":
    infile, user, pwd, db, host, search, replace = sys.argv[1:]
    subprocess.call(
        ("mysql -h {host} -u {user} --password={pwd} {db}"
         .format(**locals()).split()),
        stdin=open(infile))
    subprocess.call(search_replace_cmd(**locals()))
    
    
