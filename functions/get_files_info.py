import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
         return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        output_lines = []
        contents = os.listdir(target_dir)
        
        for item in sorted(contents):
            # Skip python cache folders
            if item == "__pycache__":
                continue
            
            full_item_path = os.path.join(target_dir, item)
            
            size = os.path.getsize(full_item_path)
            is_dir = os.path.isdir(full_item_path)

            output_lines.append(f"  - {item}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(output_lines)
    except Exception as e:
       return f"Error listing files: {str(e)}"