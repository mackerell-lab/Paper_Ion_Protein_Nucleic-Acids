
#!/bin/bash

for files in $(ls -d */* ); do
    original="stream ../toppar.str"
    replace="stream ../../../toppar.str"

    echo "$files"
    sed  -i "s|$original|$replace|" "${files%/}/ener.inp"
done

