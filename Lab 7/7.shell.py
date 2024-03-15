import subprocess
import shlex

def execute_command(command):
    try:
        # Splitting the command into a list of arguments
        args = shlex.split(command)
        
        # Execute the command
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Returning the result
        return result.stdout.decode(), result.stderr.decode()
    except Exception as e:
        return str(e), ""

def main():
    while True:
        # User input
        user_input = input("Shell> ")

        # Checking for input/output redirection
        if '>' in user_input:
            command, output_file = user_input.split('>', 1)
            command = command.strip()
            output_file = output_file.strip()
            result, error = execute_command(command)
            if error:
                print(error)
            else:
                with open(output_file, 'w') as file:
                    file.write(result)
        elif '<' in user_input:
            command, input_file = user_input.split('<', 1)
            command = command.strip()
            input_file = input_file.strip()
            with open(input_file, 'r') as file:
                result, error = execute_command(command)
                if error:
                    print(error)
                else:
                    print(result)
        elif '|' in user_input:
            commands = user_input.split('|')
            prev_output = None
            for cmd in commands:
                cmd = cmd.strip()
                result, error = execute_command(cmd)
                if error:
                    print(error)
                    break
                elif prev_output:
                    prev_output = subprocess.Popen(shlex.split(cmd), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    prev_output.stdin.write(prev_output.stdout.read())
                    prev_output.stdin.close()
                else:
                    prev_output = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if prev_output:
                print(prev_output.stdout.read().decode())
        else:
            result, error = execute_command(user_input)
            if error:
                print(error)
            else:
                print(result)

if __name__ == "__main__":
    main()
