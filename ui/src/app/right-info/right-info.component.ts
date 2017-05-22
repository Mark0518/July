import { Component, OnInit } from '@angular/core';
import { element } from 'protractor';

@Component({
  selector: 'app-right-info',
  templateUrl: './right-info.component.html',
  styleUrls: ['./right-info.component.css']
})
export class RightInfoComponent implements OnInit {
  private tags: string[] = [
    'About',
    'Centos',
    'Python',
    '字符集',
    'Nfs',
    'Rsync',
    'Inotify',
    '主从同步',
    '正则表达式',
    'Curl',
    'Python全栈之路',
  ];

  private links = [
    {'name': '算法之道', 'desc': '业余机器学习、Python和算法爱好者', 'url': '#'},
    {'name': '安生', 'desc': '大好时光！', 'url': '#'}
  ];

  private categorys = [
      {'name': 'Python', 'count': '200', 'url': '#'},
      {'name': 'Linux', 'count': '320', 'url': '#'},
      {'name': 'Django', 'count': '35', 'url': '#'},
      {'name': 'PHP', 'count': '35', 'url': '#'}
    ];

  private isShowLoginElement: Boolean = false;
  private isShowRegisterElement: Boolean = false;
  private isShowRestPasswordElement: Boolean = false;

  constructor() { }
  ngOnInit() {
  }

  isShowLogin() {
    this.isShowLoginElement = !this.isShowLoginElement;
    this.isShowRegisterElement = false;
    this.isShowRestPasswordElement = false;
  }

  isShowRegister() {
    this.isShowRegisterElement = !this.isShowRegisterElement;
    this.isShowLoginElement = false;
    this.isShowRestPasswordElement = false;
  }

  isShowRestPassword() {
    this.isShowRestPasswordElement = !this.isShowRestPasswordElement;
    this.isShowLoginElement = false;
    this.isShowRegisterElement = false;
  }
}
