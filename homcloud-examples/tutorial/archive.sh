#!/bin/sh

git archive --worktree-attributes -o pointcloud-example.zip HEAD pointcloud/
git archive --worktree-attributes -o binary-image-example.zip HEAD binary-image/
git archive --worktree-attributes -o grayscale-example.zip HEAD grayscale-image/
zip -d pointcloud-example.zip \*/.gitignore
zip -d binary-image-example.zip \*/.gitignore
zip -d grayscale-example.zip \*/.gitignore
