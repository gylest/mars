
namespace BulkLoading.UI
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnRowBy = new System.Windows.Forms.Button();
            this.btnBulk = new System.Windows.Forms.Button();
            this.labElapsedTime1 = new System.Windows.Forms.Label();
            this.labElapsedTime2 = new System.Windows.Forms.Label();
            this.txtRowElapsed = new System.Windows.Forms.TextBox();
            this.txtBulkElapsed = new System.Windows.Forms.TextBox();
            this.btnCreate = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnRowBy
            // 
            this.btnRowBy.Location = new System.Drawing.Point(78, 71);
            this.btnRowBy.Name = "btnRowBy";
            this.btnRowBy.Size = new System.Drawing.Size(104, 23);
            this.btnRowBy.TabIndex = 0;
            this.btnRowBy.Text = "Row by Row";
            this.btnRowBy.UseVisualStyleBackColor = true;
            this.btnRowBy.Click += new System.EventHandler(this.btnRowBy_Click);
            // 
            // btnBulk
            // 
            this.btnBulk.Location = new System.Drawing.Point(78, 111);
            this.btnBulk.Name = "btnBulk";
            this.btnBulk.Size = new System.Drawing.Size(104, 23);
            this.btnBulk.TabIndex = 1;
            this.btnBulk.Text = "Bulk";
            this.btnBulk.UseVisualStyleBackColor = true;
            this.btnBulk.Click += new System.EventHandler(this.btnBulk_Click);
            // 
            // labElapsedTime1
            // 
            this.labElapsedTime1.AutoSize = true;
            this.labElapsedTime1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.labElapsedTime1.Location = new System.Drawing.Point(231, 75);
            this.labElapsedTime1.Name = "labElapsedTime1";
            this.labElapsedTime1.Size = new System.Drawing.Size(92, 15);
            this.labElapsedTime1.TabIndex = 2;
            this.labElapsedTime1.Text = "Elapsed Time (s)";
            // 
            // labElapsedTime2
            // 
            this.labElapsedTime2.AutoSize = true;
            this.labElapsedTime2.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.labElapsedTime2.Location = new System.Drawing.Point(231, 115);
            this.labElapsedTime2.Name = "labElapsedTime2";
            this.labElapsedTime2.Size = new System.Drawing.Size(92, 15);
            this.labElapsedTime2.TabIndex = 3;
            this.labElapsedTime2.Text = "Elapsed Time (s)";
            // 
            // txtRowElapsed
            // 
            this.txtRowElapsed.Enabled = false;
            this.txtRowElapsed.Location = new System.Drawing.Point(390, 71);
            this.txtRowElapsed.Name = "txtRowElapsed";
            this.txtRowElapsed.Size = new System.Drawing.Size(269, 23);
            this.txtRowElapsed.TabIndex = 4;
            // 
            // txtBulkElapsed
            // 
            this.txtBulkElapsed.Enabled = false;
            this.txtBulkElapsed.Location = new System.Drawing.Point(390, 111);
            this.txtBulkElapsed.Name = "txtBulkElapsed";
            this.txtBulkElapsed.Size = new System.Drawing.Size(269, 23);
            this.txtBulkElapsed.TabIndex = 5;
            // 
            // btnCreate
            // 
            this.btnCreate.Location = new System.Drawing.Point(78, 31);
            this.btnCreate.Name = "btnCreate";
            this.btnCreate.Size = new System.Drawing.Size(104, 23);
            this.btnCreate.TabIndex = 6;
            this.btnCreate.Text = "Create Table";
            this.btnCreate.UseVisualStyleBackColor = true;
            this.btnCreate.Click += new System.EventHandler(this.btnCreate_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(780, 250);
            this.Controls.Add(this.btnCreate);
            this.Controls.Add(this.txtBulkElapsed);
            this.Controls.Add(this.txtRowElapsed);
            this.Controls.Add(this.labElapsedTime2);
            this.Controls.Add(this.labElapsedTime1);
            this.Controls.Add(this.btnBulk);
            this.Controls.Add(this.btnRowBy);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Name = "MainForm";
            this.Text = "SQL Server : Insert vs Bulk Loading Performance Test";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnRowBy;
        private System.Windows.Forms.Button btnBulk;
        private System.Windows.Forms.Label labElapsedTime1;
        private System.Windows.Forms.Label labElapsedTime2;
        private System.Windows.Forms.TextBox txtRowElapsed;
        private System.Windows.Forms.TextBox txtBulkElapsed;
        private System.Windows.Forms.Button btnCreate;
    }
}

