import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {BlogComponent} from "./blog/blog.component";
import {NotFoundComponent} from "./not-found/not-found.component";
import { ArticleComponent } from './article/article.component';
import { AdminComponent } from './admin/admin.component';

const routes: Routes = [
  {path: '', component: BlogComponent},  // 博客首页
  {path: 'article', component: ArticleComponent},  // 文章页
  {path: 'admin', component: AdminComponent},  // 后台管理
  {path: '**', component: NotFoundComponent},  // 404
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
