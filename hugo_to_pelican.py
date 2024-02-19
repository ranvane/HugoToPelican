import yaml
import re
from slugify import slugify
import os


def copy_dir_structure_and_list_files(src, dst):
    # 创建目标根目录（如果不存在）
    if not os.path.exists(dst):
        os.makedirs(dst)

    # 遍历源文件夹及其所有子文件夹，同时收集所有文件名
    all_file_paths = []
    for root, dirs, files in os.walk(src):
        # 根据源文件夹的相对路径创建目标子文件夹
        relative_path = os.path.relpath(root, src)
        target_subdir = os.path.join(dst, relative_path)

        # 如果目标子文件夹不存在，则创建
        os.makedirs(
            target_subdir, exist_ok=True
        )  # 使用exist_ok=True避免已存在时抛出错误

        # 收集当前目录下的所有文件的绝对路径
        file_paths_in_current_dir = [os.path.join(root, file) for file in files]
        all_file_paths.extend(file_paths_in_current_dir)

    return all_file_paths


def extract_hugo_metadata_and_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 分离 YAML 元数据与内容
    metadata_pattern = r"^---\n(.*?\n?)^---\n"
    match = re.match(metadata_pattern, content, re.DOTALL | re.MULTILINE)

    if match:
        metadata_str = match.group(1)
        metadata = yaml.safe_load(metadata_str)

        # 去掉元数据部分后剩下的就是正文
        content_body = content[match.end() :]

        return metadata, content_body
    else:
        raise ValueError(
            f"File {file_path} doesn't seem to have a valid Hugo front matter."
        )


def write_peclican(file_path, metadata, markdown_content):

    with open(file_path, "w", encoding="utf-8") as file:

        file.write(f"Title: {metadata['title']}\n")
        file.write(f"Date: {metadata['date']}\n")
        file.write(f"Modified: {metadata['date']}\n")
        file.write(f"Slug: {slugify(metadata['title'])}\n")

        file.write(f"Category: {' '.join(metadata['categories'])}\n")
        file.write(f"Tags: {','.join(metadata['tags'])}\n")

        file.write("\n\n")
        file.write(markdown_content)


if __name__ == "__main__":
    # 使用方法：
    source_folder = ".../hugo_blog/content/post"
    destination_folder = ".../pelican_blog/content"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)  # 确保目标文件夹存在
    file_paths = copy_dir_structure_and_list_files(source_folder, destination_folder)
    print("file_paths:", file_paths)

    for file_path in file_paths:
        if file_path.endswith(".md"):
            metadata, markdown_content = extract_hugo_metadata_and_content(file_path)

            write_peclican(
                file_path.replace(source_folder, destination_folder),
                metadata,
                markdown_content,
            )
