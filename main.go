package gopypwsh

import (
        "os/exec"
        "bytes"
        "strings"
        "errors"
        "fmt"
)

func runCommand(args []string) (string, error) {
        cmd := exec.Command("/usr/bin/python3", args...)

        var out bytes.Buffer
        var err bytes.Buffer

        cmd.Stdout = &out 
        cmd.Stderr = &err
        cmd.Run()

        // convert err to an error type if there is an error returned
        var e error
        if err.String() != "" {
                e = errors.New(err.String())
        }

        return strings.TrimRight(out.String(), "\r\n"), e
}

func RunPyCommandCreate(username string, password string, target string, cmd string, py string ) (string, error) {
        dnscmd := []string{py,"--user",username,"--password",password,"--target",target,"--command",cmd}
        out, err := runCommand(dnscmd) 
        fmt.Println(out)
        fmt.Println(err)
        return out, err
}

