import {Component, OnInit} from "@angular/core";

@Component({
  selector: 'app-article-list',
  templateUrl: './article-list.component.html',
  styleUrls: ['./article-list.component.css']
})
export class ArticleListComponent implements OnInit {
  private articles: Article[] = [
    new Article('1', "2017-05-14 18:05:29", "Python全栈之路系列之基础篇", 30),
    new Article('2', "2017-05-14 18:05:29", "Python全栈之路系列之数字数据类型", 135),
    new Article('3', "2017-05-14 18:05:29", "Python全栈之路系列之字符串数据类型", 3211111),
    new Article('4', "2017-05-14 18:05:29", "Python全栈之路系列之列表数据类型", 623),
    new Article('5', "2017-05-14 18:05:29", "Python全栈之路系列之字典数据类型", 134),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
    new Article('6', "2017-05-14 18:05:29", "Python全栈之路系列之Win字符编码深解", 30),
  ];

  constructor() {
  }

  ngOnInit() {
  }
}

export class Article {
  constructor(public url: string,
              public create_time: string,
              public title: string,
              public click_num: number) {
  }
}
