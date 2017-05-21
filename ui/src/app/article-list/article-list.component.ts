import {Component, OnInit} from "@angular/core";
import { IPageChangeEvent } from '@covalent/core';

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
  private event: IPageChangeEvent;
  private firstLast: Boolean = true;  // 显示或隐藏跳转到最后一页和第一页按钮
  private pageSizeAll: Boolean = true;  // 显示或隐藏'全部'菜单项
  private pageSizes: Number[] = [10, 20, 30, 50, 100];  // 没页显示多少条
  private total: Number = 230;  // 总条数
  private initialPage: Number = 1;  // 默认页数
  private pageSize: Number = 10;  // 默认每页显示多少条
  private pageSizeAllText: String = '全部';

  change(event: IPageChangeEvent): void {
    this.event = event;
    console.log(this.event);
  }

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
