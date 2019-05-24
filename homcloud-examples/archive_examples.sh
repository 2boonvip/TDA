#!/bin/sh

git archive --worktree-attributes --format=zip HEAD . --prefix=homcloud-examples/ -o homcloud-examples.zip
